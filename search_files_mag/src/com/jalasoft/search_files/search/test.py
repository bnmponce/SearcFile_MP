import os

st = os.stat("D:\\behave\\TestPlanv1.0.xlsx")
uid = st.st_uid
gid = st.st_gid
print(uid)
print(gid)

