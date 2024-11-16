from bs4 import BeautifulSoup
import csv

with open('data/out/Doctors_static.csv', 'w', newline='') as csvfile:
    doctorwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    maxfiles = 7
    for i in range(1, maxfiles + 1, 1):
        with open(f"data/in/Arztsuche{i}.html", 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'lxml')

            for doctor in soup.find_all('div', class_='m-react-doctors__item-wrapper'):
                details_element = doctor.find('a', class_='m-react-doctors__item-link')
                distance_element = doctor.find('div', class_='m-react-doctors__item-header-distance-km')
                doctorname_element = doctor.find('h3', class_='m-react-doctors__item-header-title-headline')
                doctortype_element = doctor.find('p', class_='m-react-doctors__item-header-title-type')
                location_element = doctor.find('div', class_='m-react-doctors__item-header-details-location')
                phone_element = doctor.find('div',
                                            class_='m-react-doctors__item-icon-link m-react-doctors__item-icon-link--phone')
                fax_element = doctor.find('div',
                                          class_='m-react-doctors__item-icon-link m-react-doctors__item-icon-link--fax')

                details = details_element.get('href').strip() if details_element else "No Details Found"
                distance = distance_element.text.strip() if distance_element else "No Distance Found"
                doctorname = doctorname_element.text.strip() if doctorname_element else "No Name Found"
                doctortype = doctortype_element.text.strip() if doctortype_element else "No Specialization Found"
                locations = [p_tag.get_text() for p_tag in
                             location_element.find_all("p")] if location_element else "No Location Found"
                phone = phone_element.text.strip() if phone_element else "No Phone Found"
                fax = fax_element.text.strip() if fax_element else "No Fax Found"

                print(f"Details: {details}")
                print(f"Distance: {distance}")
                print(f"Doctor Name: {doctorname}")
                print(f"Doctor Type: {doctortype}")
                print(f"Street: {locations[0]}")
                print(f"City: {locations[1]}")
                print(f"Phone: {phone}")
                print(f"Fax: {fax}")

                doctorwriter.writerow([details, distance, doctorname, doctortype, locations[0], locations[1], phone, fax])
