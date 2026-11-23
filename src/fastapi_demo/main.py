from fastapi import FastAPI, Request,status, Path as Fpath, Query
import json
from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from helper.get_json_data import get_students_data, get_student
from starlette.exceptions import HTTPException

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code= exc.status_code,
        content={'message':str(exc.detail)}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request, exc:RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={"message": "Invalid input, please enter valid input."}
    )



@app.get('/')
def getURL():
    return {'Success':200,'message':'Data fetch successfully'}

json_path =  Path(__file__).resolve().parent.parent / 'data'/ 'student.json'
@app.get('/student')
def getStudents():
    return get_students_data()


@app.get('/student/{id}')    # below Fpath we use to set indication inside the docs allow to strictly required field
                            # only visible in /docs not for url base search

                            #it is path parameter so we use Path (Fpath)
def getStudent(id:int = Fpath(...,description='id integer required', examples=[1])):
    student = get_student(id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not Found.")
    return student

@app.get('/genderdata') #here gener is query parameter so we use Query as like path
                        #Instead of ... (compaulsory) we use None default value
def getGenderWiseData(gender:str = Query(None,description='Enter gender after URL',openapi_examples={ "male": {"summary": "Male", "value": "Male"}, "female":{"summary":"Female",'value':'Female'}})):
    students = get_students_data()

    if students is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found.')
    
    if gender is None:
        return students
    
    filterData = []
    for student in students:        #casefold() converts a string to a normalized lowercase form for case-insensitive comparisons.
        if student['gender'].casefold() == gender.strip().casefold():
            filterData.append(student)
    return filterData

# -------------Sort and Order by Query parameter------------
SORT_FIELDS = ['name','age']
SORT_ORD = ['asc','desc']

@app.get('/sort')
def getSortedData(sort_by:str = Query(
                                        ...,
                                        openapi_examples={
                                            "name": {"summary": "Sort by name", "value": "name"},
                                            "age": {"summary": "Sort by age", "value": "age"},
                                        },
                                    ),
                  sort_ord:str = Query(...,openapi_examples={'asc':{'summary':'Ascending','value':'asc'},
                                                             'desc':{'summary':'Descending','value':'desc'}})):

    if sort_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Check sort by field"
        )

    if sort_ord not in SORT_ORD:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Please check sort by value: {sort_by} it is not in fields'
        )

    data = get_students_data()

    reverse = (sort_ord == 'desc')

    return sorted(data,key=lambda s:s[sort_by],reverse=reverse)
    

@app.get('/pagination')
def pagination(page:int = Query(1,ge=1,description='Enter Page No:')     #ge =(greater than equel to >=) and le = (less than equel to <=)
                ,limit:int = Query(5,ge=2,le=10)):
    data = get_students_data()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Data Not Found."
        )

    start = (page-1)*limit
    end = start + limit
    page_wise_data = data[start:end]

    return page_wise_data


def main():
    print('JAY SHREE RAM')


if __name__ == '__main__':
    main()