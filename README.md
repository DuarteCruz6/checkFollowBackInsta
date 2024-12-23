# THIS PROGRAM WILL TELL YOU WHO DOES NOT FOLLOW YOU BACK
## EXPLANATION

Have you ever been curious about who doesn't follow you back on Instagram, but you were to lazy to check one by one? Well, me too. So I decided to create this program that creates a file containing both the username as well as the link to the people who don't follow you back. 
Instagram now lets you download your account's information in a .json file. Therefore, by downloading the files containing who follows you, as well as the files containing who you follow, we can check who follows/doesn't follow you back. 

## TUTORIAL
### DOWNLOADING .JSON FILES
To start this program, first of all you need to clone this repository to a folder. After that, you just need download the files containing your information.
##### Step 1: 
  Go to your profile and click on these three lines.  ![alt text][photo1]
##### Step 2:
  Open your account center. ![alt text][photo2]
##### Step 3:
  Click in "Your information and permissions". ![alt text][photo3]
##### Step 4:
  Press "Download your information". ![alt text][photo4]
##### Step 5:
  Press "Download or transfer information". ![alt text][photo5]
##### Step 6:
  Click "Some of your information", since we only need the files containing who follows you and who you follow. ![alt text][photo6]
##### Step 7:
  Scroll down until you see the "Connections" sections and go ahead and tick "Followers and following". After ticking, press "Next". ![alt text][photo7]
##### Step 8:
 Select what option you prefer. For this tutorial I selected "Download to device", but either are corrected and will work ![alt text][photo8]
##### Step 9:
 Click on "Date range". ![alt text][photo9]
##### Step 10:
 Select "All time". If you select another option, the files won't contain your oldest followers and accounts you have been following for a while. Ater selecting, press "Save". ![alt text][photo10]
##### Step 11:
 Click "Format". After clicking, select "JSON". ![alt text][photo11]
##### Step 12:
If your screen looks like this: ![alt text][photo12], you are good to go. Check if your "Notify" e-mail is correct, if so, click "Create files". You will receive an email from Instagram-Meta containing a link to download your files.
##### Step 13:
After receiving the email, click on "Download your information". It will open up a link from Instagram in which you are going to click on "Download". If it requests your password, type it in and press "Continue".
##### Step 14:
Save the downloaded file in the "checkFollowBack" folder. This folder now must contain the file code.py as well as the .zip file.
##### Step 15:
Unzip the file. You can delete the .zip file if your OS doesn't delete it automatically. Your checkFollowBack folder now should have the code.py file, as well as the "connections" folder inside it. If it looks like this, you are good to go. ![alt text][photo13].

### RUNNING THE PROGRAM
##### Step 1:
Open your terminal. If you are on a MacOS, open your Apps on Finder and search for Terminal. If you are in Windowns, type cmd on your search bar and click enter and "Command Prompt" shows up.
##### Step 2:
Write "cd " on the terminal and drag and drop the checkFollowBackInsta folder to your terminal. When dropped, click Enter.
##### Step 3:
Write "python ./code.py" on your terminal and click enter. If the Terminal says permission denied, then write this command "chmod +x code.py" and try again. If nothing shows up in your terminal, then everything went well. The code now created a file named peopleWhoDontFollowYouBack on the checkFollowBack folder.
##### Step 4:
The code now created a file named peopleWhoDontFollowYouBack on the checkFollowBack folder. This folder contains every username+link of the people who do not follow you back.

[photo1]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo1.JPG "Click on these three lines"
[photo2]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo2.JPG "Click on Accounts Center"
[photo3]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo3.JPG "Click on Your information and permissions"
[photo4]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo4.JPG "Click on Download your information"
[photo5]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo5.JPG "Click on Download or transfer information"
[photo6]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo6.JPG "Click on Some of your information"
[photo7]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo7.JPG "Scroll down and select Followers and following"
[photo8]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo8.JPG "Choose whatever option you desired. I choose Download to device"
[photo9]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo9.JPG "Click on Date range"
[photo10]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo10.JPG "Select All time"
[photo11]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo11.JPG "Click on Format"
[photo12]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo12.JPG "How it should look like"
[photo13]: https://github.com/DuarteCruz6/checkFollowBackInsta/blob/main/photos/photo13.JPG "Three lines you need to click on"
