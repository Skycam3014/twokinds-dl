import requests


def check_url(url):
    request = requests.get(url)
    print('Checking for content at: ' + url)
    if request.status_code == 200:
        print('Content found at: ' + url + '/ attempting to download...')
        return True
    else:
        print('Unable to find content at: ' + url + '/ proceeding...')
        return False


def increase_date(date):
    date = str(date)
    year = date[:4]
    monthday = date[:6]
    month = monthday[-2:]
    day = date[-2:]

    year = int(year)
    month = int(month)
    day = int(day)

    day += 1

    if day > 31:
        day = '01'
        month += 1
        if month > 12:
            month = '01'
            year += 1

    year = str(year)
    month = str(month)
    day = str(day)

    if len(month) == 1:
        month = '0' + month

    if len(day) == 1:
        day = '0' + day

    date = year + month + day
    date = str(date)
    date = int(date)

    return date


# Main

# Check Url
panelDate = 20031022
panelNumber = 1

panelUrl = 'https://cdn.twokinds.keenspot.com/comics/' + str(panelDate)

while panelDate != '20210415':
    if check_url(panelUrl):
        content = requests.get(panelUrl)
        contentName = 'twokinds_' + str(panelNumber) + '.jpg'
        open(contentName, 'wb').write(content.content)
        panelNumber += 1
        panelDate = increase_date(panelDate)
        print('Date incremented...')
    else:
        panelDate = increase_date(panelDate)
        print('Date incremented...')

    panelUrl = 'https://cdn.twokinds.keenspot.com/comics/' + str(panelDate)