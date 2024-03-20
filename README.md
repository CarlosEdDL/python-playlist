# python-playlist
In order to use this script, you need to do a few things. 
## Create a spotify app. 
Go to https://developer.spotify.com/dashboard and sign in with you spotify account, then click on the ''create app'' button (you might need to verify your email address for this step).
Choose an app name and app description. In the redirect URI, write http://example.com
In the 'Which API/SDKs are you planning to use?' window, choose all the options. Then, agree with Spotify's terms, and click save.

## Get your credentials
After successfully creating an app, click on settings, copy the client ID, and paste it into the CLIENT_ID variable in the script.
Then, copy the Client Secret and paste it into the CLIENT_SECRET variable in the script.
Finally, in the USERNAME variable, write your spotify username.

If you run the scrip at this point, you will be redirected to a confirmation page. 
Click on the Agree button, and then you will be sent to an ''Example domain page'' 
Copy the whole URL of that page, paste it into the '' Enter the URL you were redirected to: '' prompt you got in your IDE, and press enter. 

## Run the program
At this point, you should be prompted to choose a date, in the YYYY-MM-DD format, that is, if you want to get the top 100 songs during May 4th of the year 2000, you should write 
2000-05-04. 
After you enter the date, what until the script stops running, and go to your spotify profile. You should see the playlist with the 100 (or less, depending on the songs availability in spotify) songs created.


