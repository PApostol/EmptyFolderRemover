import os, sys

# removes empty directories recursively
def remove_empty(dir_path, counter):
    try:
        if not os.path.isdir(dir_path):
            return False

        if all([remove_empty(os.path.join(dir_path, filename), counter) for filename in os.listdir(dir_path)]):        
            counter[0]+=1
            os.rmdir(dir_path)
            counter[1]+=1
            return True
        else:
            return False
    except:
        counter[2]+=1


def main():
    args = sys.argv[0:] # cmd arguments
    counter = [0, 0, 0] # [found, deleted, denied]

    if len(args)==1:
        print('Working, please wait...')
        remove_empty('.', counter)

    elif len(args)==2:
        print('Working, please wait...')
        remove_empty(args[1], counter)

    else:
        print('Too many arguments!')
        sys.exit()

    print('\nFinished.')
    print('Found ' + str(counter[0]) + ' empty directories.')
    print('Deleted ' + str(counter[1]) + ' empty directories.')

    if counter[2]>0:
        print('Permission to access or delete some directories was denied.')


if __name__ == '__main__':
    main()