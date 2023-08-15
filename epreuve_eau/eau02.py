import sys

if __name__ == "__main__":

    params = list(sys.argv[1:])

    params = params[::-1]
    params = " ".join([str(item) for item in params])

    print(params)