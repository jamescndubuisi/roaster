from numba import jit
import pandas
import uuid
# involve locations and time
# @jit(nopython=True, parallel= True, cache= True, nogil = True)
def file_handler(file):
    file.columns = [str(x).lower() for x in file.columns]
    print(file)
    if "name" in file.columns:
        name = file["name"]
    else:
        name = file["fullname"]
    rank = file["rank"]
    phone_number = file["phone"]
    email = file["email"]
    department = file["department"]
    gender = file['gender']


    data_frame = pandas.concat([name, rank, phone_number, email, department, gender], axis=1)
    data_frame.rename(columns={"phone": "phone number"}, inplace=True)
    data_frame['batch'] = 0
    batch = data_frame.batch.apply(lambda x: uuid.uuid4().hex)
    data_frame['batch'] = batch
    print(data_frame)
    return data_frame
   