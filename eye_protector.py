import time as T

def ask_for_start_now():
    return input("Do you want to start eye protection exercise now ?")

def run_youtube():
    T.sleep(200)
    input("You should be done now, well done!")


while True:
    ans = ask_for_start_now()

    if ans.lower() == "y":
        run_youtube()
        break
    else:
        T.sleep(60)