def isNum(str):
    try:
        int(str)
    except:
        try:
            float(str)
        except:
            try:
                complex(str)
            except:
                return False
    else:
        return True