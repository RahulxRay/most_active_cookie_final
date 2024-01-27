import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Find the most active cookie in a log file for a given date.')
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-d', '--date', type=str, required=True)
    return parser.parse_args()

def main():
    args = parse_arguments()
    date = args.date
    
    filename = args.file
    
    all_data = list(open(filename, 'r'))
    all_data = all_data[1:] # Removes cookie, timestamp from the data


    count = get_count(all_data,date) # get count of all cookie

    most_active = get_most_active(count)

    
    for cookie in most_active:
        print(cookie)

def get_count(all_data,date):
    count = {}
    for l in all_data:
        cookie,timestamp = l.strip().split(',')
        #print(cookie)
        cookie_date = timestamp.split('T')[0]
        #print(cookie_date)
        if cookie_date == date:
            if cookie in count:
                count[cookie] += 1
            else:
                count[cookie] = 1
    return count

def get_most_active(count):
    max_count = 0
    most_active = []

    for i in count:
        if count[i] > max_count:
            most_active = []
            most_active.append(i)
            max_count = count[i]
        elif count[i] == max_count:
            most_active.append(i)

    return most_active
    
   
if __name__ == '__main__':
    main()
