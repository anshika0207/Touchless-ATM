# Touchless - ATM
## Inspiration
Coronavirus has affected millions of people around the globe and is rising at a very high pace. With Coronavirus being the highlight of recent times, our team realized that the major cause of widespread of this virus is contact in public places.So we developed this project to eradicate the need of contact on essential places, one of them being banks. Access to cash for many in society is remaining essential during the current lockdown around the globe. Studies worldwide on the virus have shown that it can remain alive up to two days on solid surfaces. Since it is not advisable to clean electronic items such as POS machines and ATMs with sanitizers after every use this project aims to ensure that bank transactions are done with minimum possible contact. Also, we further aim to expand our project to workplaces, restaurants and beyond.

## What we built?
An ATM uses buttons to read user's input. To remove this human contact during the process of transaction, we developed an ATM simulation that can be used without touching the buttons. Only through easy and minimal hand gestures, one can operate this ATM. It requires only a webcam access.

## Tech Stack
* Python
* Opencv
* MediaPipe
* Tkinter


## Installation

1. Fork this repository .     (Using Fork option on the top right corner of the repository)

2. Clone the forked repository in your local.  (Use the command given below)
```
  git clone   https://github.com/anshika0207/AMOC-2021
```
3. Navigate to the project directory.
```
cd  AMOC-2021/ATM
```

4. Setting up venv-environment in your local.

```
python3 -m venv env             (Create a separate Environment)
```
```
source env/bin/activate           (Activate the environment)
```
```
pip3 install -r requirements.txt  (Install's the dependencies)
```
 5.  Now you are set and can run the python scripts with
```
python3  ATM_system.py


````
## Presentation Video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/UYBnKTiNJrc/0.jpg)](https://www.youtube.com/watch?v=UYBnKTiNJrc)
## Challenges we faced!
* We faced challenges while getting individual co-ordinates of each point on hand from the model. So after extensive searching we found methods of extracting a single landmark, so that instead of working with the 21 detected coordinates, only those useful to us were used.
* While working with Tkinter, we faced difficulties in giving functionality to our ATM GUI. We slved this issue by referring the documentation of Tkinter.
* Deciding a reference point was again a challenge as, we had to find a coordinate that remains stable while performing gestures, i.e., during click. Finally we chose three coordinates, along the corners of our palm and generated a point equidistant from these three coordinates. This point was then used as our mouse.
* The final challenge was integrating both python scripts and then to run them simultaneously. To overcome this, we used threading.

## So what's next?
* We plan to expand this project on other public places like restaurants, lifts and public transports.
* We aim to make the ATM GUI more interactive and user-friendly.
* We further aim to store user’s information in a database.

## Contributers:
* Pooja Paliwal
* Anshoo Rajput
* Anshika Bhatt
