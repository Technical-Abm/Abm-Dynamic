import platform
abm = platform.architecture()[0]
if "64bit" in abm:
  from abm64bit import main
  main()
else:
  print()
  print("Invalid aarch device please try again")
  exit()
