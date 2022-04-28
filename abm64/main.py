import platform
abm = platform.architecture()[0]
if "64bit" in abm:
  from abm64bit import User_select
  User_select()
else:
  print()
  print("Invalid aarch device please try again")
  exit()
