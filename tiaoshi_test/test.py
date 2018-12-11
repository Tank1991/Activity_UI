

for i in range(10):
    js = 'document.getElementsByClassName("el-select-dropdown el-popper")[%s].style.display= "none"'%i
    print(js)
