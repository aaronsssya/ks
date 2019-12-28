def message(m):
    try:
        return(str(m))
    except:
        return('error')

if __name__ == '__main__':
    message('hello world')