import platform
abm = platform.architecture()[0]
if "32bit" in abm:
  from abm32bit import main
  main()
else:
  print()
  print("Invalid aarch device please try again")
  exit()
