# Nearest holiday application

This is a simple app created with flask, calendarific.com API and Docker.

## Description

This app will show you the nearest holiday that is celebrated in specified country.

## Getting Started

### Dependencies

* Python version: 3.8
* Flask version: 2.0.1
* Docker version: 20.10.8

### Executing program

```
docker run -e API_KEY=/your_api_key/ -e MY_NAME=/your_name/ -e COUNTRY=/your_country/ /image-name/
```

### Help

You can choose whatever country you want by using [ISO-3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).\
Some examples:

| Country        | ISO-3166       |
| -------------- |:--------------:|
| Russia         | RU             |
| United States  | US             |
| United Kingdom | GB             |
| Germany        | DE             |
| France         | FR             |
| Finland        | FI             |
