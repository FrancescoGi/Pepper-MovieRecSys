# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:06:09 2018

@author: Francesco & Piero
"""
import datetime
from urllib import quote

def generate_message_id():
    id=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    return id
    
def sublist(lst1, lst2):
   ls1 = [element for element in lst1 if element in lst2]
   return list(set(ls1)) == list(set(lst2))
   
def choose_html(msg,filename):

        id = 0
        try:
            keyboard=msg['reply_markup']['keyboard']
        except:
            keyboard=[]

        try:
            link=msg['messages'][1]['link']
        except:
            link=''
                
        try:
            if len(msg['messages']) <= 3:
                suggest=msg['messages'][1]['photo']
                say=msg['messages'][0]['text']
            else:
                suggest=msg['messages'][2]['photo']
                say=msg['messages'][0]['text']+'\n'+msg['messages'][1]['text']                
                del msg['messages'][0]
        except:
            suggest=''
            say=''

        if keyboard != []:
            if len(msg['messages']) > 2:
                say = msg['messages'][0]['text']
                del msg['messages'][0]
                id = html_alternatives(msg,filename)
                return 1, id, str(say)+'\n'+str(msg['messages'][0]['text'])
                        
            else:
                id = html_alternatives(msg,filename)
                return 1, id, msg['messages'][0]['text']
  
        elif suggest != '':
            id = html_suggestion(msg, filename) 
            return 2, id, say

        elif link != '':
            id = html_trailer(msg, filename) 
            return 3, id, 'What do you think about this movie?'           

        else:
            if msg['messages'][0]['text'] == 'Ok, here are all your ratings:':
                id = html_profile(msg, filename) 
                return 4, id, msg['messages'][0]['text']+'\n'+ msg['messages'][2]['text']         
            else:    
                return 0, id, msg['messages'][0]['text']



def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    #webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac        
        
def html_alternatives(msg, filename):
    l = len(msg['reply_markup']['keyboard'])
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Pepper</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
        
        <script src="/libs/qi/2/qi.js"></script>
           <script>
            function choice(string){
                
                string = string.replace(/%27/g,"'").replace(/%28/g,"(").replace(/%29/g,")").replace(/%20/g," ").replace(/%3A/g,":");
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
    
                    m.insertData("'''+id+'''",string);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
        </script> 
    </head>
    <body>

    <div class="container">
        <div style="text-align:center;">
            <h2 style="font-family: Poppins-Bold;">'''+msg['messages'][0]['text'].encode('ascii','ignore')+'''</h2>
        </div><br><br>'''
        
    for i in range(l):
        contents = contents+'''<div class="row" style="margin-right:auto; margin-left:auto;">
            <h3><u><a href="#" onClick='choice("'''+quote(msg['reply_markup']['keyboard'][i][0].encode('ascii','ignore'))+'''")'><b>'''+msg['reply_markup']['keyboard'][i][0].encode('ascii','ignore')+'''</b></a></u></h3>
        </div>'''

        
    contents=contents+'''</div>
        <div style="text-align:center;"><button onClick='choice("Skip")' class="skip">
            <i class="fas fa-angle-double-right" aria-hidden="true"></i>
            Skip
        </button></div>
    </body>
    </html>
    '''
    browseLocal(contents,filename)
    return id

def html_profile(msg, filename): 
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Pepper</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="css/style.css">
         <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
       
        <script src="/libs/qi/2/qi.js"></script>
           <script>
            function choice(string){
                
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
    
                    m.insertData("'''+id+'''",string);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
        </script> 
    </head>
    <body>

    <div class="container">
        <div style="text-align:center;">
            <h2 style="font-family: Poppins-Bold;">'''+msg['messages'][0]['text'].encode('ascii','ignore')+'''</h2>
        </div><br><br>
                
        <pre style="font-size: 18px; background-color: white; border: 0px;" >'''+msg['messages'][1]['text']+'''</pre>'''    
    contents = contents+'''<div style="text-align: center;">
        <h4><b>Just press the button "Okay" to continue.</b></h4>
        <button onClick='choice("Okay")' class="skip" id="skip">
            <i class="fas fa-angle-double-right" aria-hidden="true"></i>
            Okay
        </button>
        </div>'''
            

    contents=contents+'''</div>

    </body>
    </html>
    '''
    browseLocal(contents,filename)
    return id


def html_suggestion(msg, filename):
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Pepper</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
        
        <script src="/libs/qi/2/qi.js"></script>
           <script>
            function choice(string){
                
                string = string.replace(/%27/g,"'").replace(/%20/g," ").replace(/%3A/g,":");
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
    
                    m.insertData("'''+id+'''",string);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
        </script> 
    </head>
    <body>

    <div class="container">
        <div style="text-align:center;">
            <h2 style="font-family: Poppins-Bold;">'''+msg['messages'][0]['text'].encode('ascii','ignore')+'''</h2>
        </div><br>'''

    contents = contents+'''<div class="row" style="margin-right:auto; margin-left:auto;">
        <h2 style="text-align:center;">'''+msg['messages'][1]['text'].encode('ascii','ignore')+'''</h2>
    </div><div class="row" style="margin-right:auto; margin-left:auto;">
        <p style="text-align:center;" ><img src="'''+msg['messages'][1]['photo']+'''" style="width:280px; height:390px;" /></p>
    </div></div>'''
    
    contents = contents+'''<div style="text-align: center;">
        <button onClick='choice("I like it")' class="like" id="like">
            <i class="far fa-thumbs-up" aria-hidden="true"></i>
        </button>

            <button onClick='choice("I do not like it")' class="dislike" id="dislike">
            <i class="far fa-thumbs-down" aria-hidden="true"></i>
        </button>

        <button onClick='choice("Skip")' class="skip" id="skip">
            <i class="fas fa-angle-double-right" aria-hidden="true"></i>
            Skip
        </button>
        <br>
        </div>
        '''


    contents=contents+'''</div>

    </body>
    </html>
    '''
    browseLocal(contents,filename)
    return id
 
def html_trailer(msg, filename):
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Pepper</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->

        <script src="/libs/qi/2/qi.js"></script>
           <script>
            function choice(string){
                
                string = string.replace(/%27/g,"'").replace(/%20/g," ").replace(/%3A/g,":");
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
    
                    m.insertData("'''+id+'''",string);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
        </script> 
    </head>
    <body>

    <div class="container">
        <div style="text-align:center;">
            <h2 style="font-family: Poppins-Bold;">Enjoy the trailer!</h2>
        </div><br><br>'''

    contents = contents+'''<div class="row" style="margin-right:auto; margin-left:auto;">
    </div><div class="row" style="margin-right:auto; margin-left:auto;">
        <p style="text-align:center;" ><iframe src="http://www.youtube.com/embed/'''+msg['messages'][1]['link'].split('=')[1]+'''" width="560" height="315" frameborder="0" allowfullscreen></iframe></p>
    </div>
        <div style="text-align: center;">
        <button onClick='choice("I like it")' class="like" id="like">
            <i class="far fa-thumbs-up" aria-hidden="true"></i>
        </button>

            <button onClick='choice("I do not like it")' class="dislike" id="dislike">
            <i class="far fa-thumbs-down" aria-hidden="true"></i>
        </button>

        <button onClick='choice("Skip")' class="skip">
            <i class="fas fa-angle-double-right" aria-hidden="true"></i>
            Skip
        </button>
        </div>
        <div style="text-align: center;">
        </br>
        <button onClick='choice("Other")' class="other" id="other">
            Press here to say something!
        </button>
        </div>
        '''


    contents=contents+'''</div>

    </body>
    </html>
    '''
    browseLocal(contents,filename)
    return id

def html_signup(filename):
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Login</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--===============================================================================================-->    
            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
        <!--===============================================================================================-->    
            <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
        <!--===============================================================================================-->    
            <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
        
        <script src="/libs/qi/2/qi.js"></script>
         <script>
            function send(){
                var firstname = document.getElementById("fname").value;
                var lastname = document.getElementById("lname").value;
                var username = document.getElementById("uname").value;
                var insert = firstname+"&"+lastname+"&"+username;
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
                
                    m.insertData("'''+id+'''",insert);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
        </script> 
                
        </head>
        <body>
            
            <div class="limiter">
                <div class="container-login100">
                    <div class="wrap-login100">
                            <span class="login100-form-title p-b-26">
                                Sign Up
                            </span>
        
                            <div class="wrap-input100 validate-input" >
                                <input class="input100" type="text" name="fname" id="fname">
                                <span class="focus-input100" data-placeholder="Firstname"></span>
                            </div>
                            <div class="wrap-input100 validate-input" >
                                <input class="input100" type="text" name="lname" id="lname">
                                <span class="focus-input100" data-placeholder="Lastname"></span>
                            </div>
                            <div class="wrap-input100 validate-input" >
                                <input class="input100" type="text" name="uname" id="uname">
                                <span class="focus-input100" data-placeholder="Username"></span>
                            </div>                    
        
        
                            <div class="container-login100-form-btn">
                                <div class="wrap-login100-form-btn">
                                    <div class="login100-form-bgbtn"></div>
                                    <button class="login100-form-btn" onClick="send()" type="submit" >
                                        Sign Up
                                    </button>
                                </div>  
                            </div>
                            <div class="text-center p-t-115" style="padding-top:0px;">
                                <span class="txt1">
                                    When you press the button stay still so that Pepper learns to recognize you.
                                </span>
                            </div>
                    </div>
                </div>
            </div>
            
        
            <div id="dropDownSelect1"></div>
            
        <!--===============================================================================================-->
            <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/animsition/js/animsition.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/bootstrap/js/popper.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/select2/select2.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/daterangepicker/moment.min.js"></script>
            <script src="vendor/daterangepicker/daterangepicker.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/countdowntime/countdowntime.js"></script>
        <!--===============================================================================================-->
            <script src="js/main.js"></script>
        
        </body>
        </html>'''
    
    browseLocal(contents,filename)
    return "Insert your Credentials.", id

def html_login_or_signup(filename):
    id = generate_message_id()
    contents = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Login</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--===============================================================================================-->    
            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
        <!--===============================================================================================-->    
            <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
        <!--===============================================================================================-->    
            <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
        
            <script src="/libs/qi/2/qi.js"></script>
            <script>
            function send(string){
                        
                var session = new QiSession();
                session.service("ALMemory").then(function (m) {
                
                    m.insertData("'''+id+'''",string);
                    m.getData("'''+id+'''").then(function(data) {
                        //document.write(data);                
                    }, console.log);
                },function(error) { 
                    document.write("No");                
                });
            }
            </script> 
                
        </head>
        <body>
            
            <div class="limiter">
                <div class="container-login100">
                    <div class="wrap-login100">
                            <span class="login100-form-title p-b-26">
                                Welcome to MovieRecSys
                            </span>
        
                            <div class="container-login100-form-btn">
                                <div class="wrap-login100-form-btn">
                                    <div class="login100-form-bgbtn"></div>
                                    <button class="login100-form-btn" onClick="send('login')" type="submit">
                                        Login
                                    </button>
                                </div>
                            </div>
        
                            <div class="text-center p-t-115">
                                <span class="txt1">
                                    Don’t have an account?
                                </span>
        
                                <u><a href="#" class="txt2" onClick="send('signup')" type="submit">
                                    Sign Up
                                </a></u>
                            </div>
                    </div>
                </div>
            </div>
            
        
            <div id="dropDownSelect1"></div>
            
        <!--===============================================================================================-->
            <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/animsition/js/animsition.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/bootstrap/js/popper.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/select2/select2.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/daterangepicker/moment.min.js"></script>
            <script src="vendor/daterangepicker/daterangepicker.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/countdowntime/countdowntime.js"></script>
        <!--===============================================================================================-->
            <script src="js/main.js"></script>
        
        </body>
        </html>
        '''
    browseLocal(contents,filename)
    return "Hello human.\n Sign Up or Login!", id

#msg = {u'messages': [{u'text': u'Which one of these do you dislike?'}, {u'text': u'A Good Year\nA Good Woman\nA Good Man'}], u'reply_markup': {u'resize_keyboard': True, u'one_time_keyboard': True, u'keyboard': [[u'A Good Year'], [u'A Good Woman'], [u'A Good Man']]}}
#msg={u'messages': [{u'text': u'You said that you like Tom Cruise, can you be more specific?'}, {u'text': u'Possible values are: producer, actor.'}], u'reply_markup': {u'resize_keyboard': True, u'one_time_keyboard': True, u'keyboard': [[u'Producer'], [u'Actor']]}}
msg={u'messages': [{u'text': u'I suggest you watch this:\n\n'}, {u'text': u'Relative Strangers', u'photo': u'https://image.tmdb.org/t/p/w500/xwzwXW5wP4HOOJnp5Fiw7ESjtnG.jpg'}, {u'text': u"What do you think of this movie? If you want, you can tell me what you like or don't like about it.\nIf you don't know, just tell me to skip it."}]}
#msg={u'messages': [{u'text': u'Ok, here are all your ratings:'}, {u'text': u'You liked The Matrix\nYou liked horror film as genre\nYou disliked Star Jones as actor\nYou disliked Titanic\nYou liked Scarface'}, {u'text': u'You can change or delete one of your preferences.\nOr you can ask me to reset your profile.'}]}
#msg={u'messages': [{u'text': u"Ok, I'll skip this."}, {u'text': u'I suggest you watch this:'}, {u'text': u'The Matrix Revolutions', u'photo': u'https://image.tmdb.org/t/p/w500/sKogjhfs5q3azmpW7DFKKAeLEG8.jpg'}, {u'text': u"What do you think of this movie? If you want, you can tell me what you like or don't like about it.\nIf you don't know, just tell me to skip it."}]}
#msg={u'messages': [{u'text': u'Which one of these do you dislike?'}, {u'text': u'Mission: Impossible\nMission: Impossible III\nMission: Impossible II\nLa Mission\nMission: Impossible 6\nMission: Impossible - Rogue Nation\nMission: Impossible \u2013 Ghost Protocol'}], u'reply_markup': {u'resize_keyboard': True, u'one_time_keyboard': True, u'keyboard': [[u'Mission: Impossible'], [u'Mission: Impossible III'], [u'Mission: Impossible II'], [u'La Mission'], [u'Mission: Impossible 6'], [u'Mission: Impossible - Rogue Nation'], [u'Mission: Impossible \u2013 Ghost Protocol']]}}
#msg={u'messages': [{u'text': u'Ok, I added a positive rating for: 10 Items or Less.'}, {u'text': u'I suggest you watch this:'}, {u'text': u'5 Flights Up', u'photo': u'https://image.tmdb.org/t/p/w500/5S3K1vpIYhFu5pJU4sxv95kTHxd.jpg'}, {u'text': u"What do you think of this movie? If you want, you can tell me what you like or don't like about it.\nIf you don't know, just tell me to skip it."}]}
#msg={u'messages': [{u'text': u'Sure! You can watch the trailer by clicking the link below:'}, {u'text': u'The Matrix Reloaded', u'link': u'http://youtube.com/watch?v=zsgrsiZoymA'}, {u'text': u"So, what do you think of The Matrix Reloaded?\nIf you want, you can tell me what you like or don't like about it.\nIf you don't know, just tell me to skip it."}]}
#print(str(msg['messages'][0]['text']))
#msg={u'messages': [{u'text': u'Sure! You can watch the trailer by clicking the link below:'}, {u'text': u'Che', u'link': u'http://youtube.com/watch?v=fqTw2dtVQzw'}, {u'text': u"So, what do you think of Che?\nIf you want, you can tell me what you like or don't like about it.\nIf you don't know, just tell me to skip it."}]}
#msg={u'messages': [{u'text': u'You said that you like Morgan Freeman, can you be more specific?'}, {u'text': u'Possible values are: actor, producer, executive producer, voice actor, director.'}], u'reply_markup': {u'resize_keyboard': True, u'one_time_keyboard': True, u'keyboard': [[u'Actor'], [u'Producer'], [u'Executive Producer'], [u'Voice Actor'], [u'Director']]}}
print(choose_html(msg,'index.html'))
#print(generate_message_id())
#print(html_signup('index.html'))
