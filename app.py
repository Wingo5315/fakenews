# Thanks to https://pythonise.com/series/learning-flask/rendering-html-files-with-flask
from flask import Flask
from flask import render_template
from flask import request
import urllib.parse
app = Flask(__name__)
@app.route('/')
def return_homepage():
    if __name__ == '__main__':
        app.run_server()
    # Return home page
    return Flask.render_template("index.html")
@app.route('/results')
def process_url():
    # The submitted URL
    the_url = request.args.get('url')
    # A tuple version of submitted URL
    full_url = urllib.parse.urlparse(the_url)
    # Define reason variable (default value is 0)
    reason = 0
    # TODO: Check if there is a TLD at the end of the primary domain (eg. http://wibble is invalid, but http://wibble.com is valid)
    dot = '.'
    if (dot in full_url.netloc):
        next
    else:
        is_valid_url = False
    # Check is URL is actually valid
    if (full_url.scheme == 'https'):
        is_valid_url = True
    elif (full_url.scheme == 'http'):
        is_valid_url = True
    else:
        is_valid_url = False
        reason = 3
    # Check if primary domain is on banned list (mainly social media and video-sharing sites)
    # TODO: Create array with banned domains in, use while or for statement to check each array value. Backup code before doing this.
    banned_counter = 0
    banned_domains = ["www.youtube.com", "youtube.com", "youtu.be", "www.vimeo.com", "vimeo.com", "www.facebook.com", "facebook.com", "l.facebook.com", "twitter.com", "t.co", "www.instagram.com", "instagram.com", "www.pinterest.com", "tiktok.com", "vm.tiktok.com"]
    while (banned_counter < 15):
        if (full_url.netloc == banned_domains[banned_counter]):
            is_valid_url = False
            reason = 1
            next
        banned_counter += 1
    # Check if URL points to video and audio content within news sites. Also check if the content is an image or video.
    video_counter = 0
    video_content_paths = ["/video/", "/video_and_audio", "/av/", "/videos/", "/audio/", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".PNG", ".JPG", ".GIF"]
    while (video_counter < 13):
        if (video_content_paths[video_counter] in full_url.path):
            is_valid_url = False
            reason = 2
            next
        video_counter += 1
    # And lastly, check if the article is an opinion (still a valid article, but users will be told it is opinion)
    opinion_paths = ["/commentisfree/", "/opinion", "/comment/", "/opinions/", "/voices/"]
    opinion_counter = 0
    # Default value of is_opinion variable set here
    is_opinion = False
    while (opinion_counter < 5):
        if (opinion_paths[opinion_counter] in full_url.path):
            is_opinion = True
            next
        opinion_counter += 1
    # Check if the reason variable has been changed
    if (reason == 1):
        reason = "it came from a video-sharing or social-media website."
        short_reason = "from social media website"
    elif (reason == 2):
        reason = "it points to a page mostly made up of videos, images or audio content."
        short_reason = "mostly videos/images/audio content"
    elif (reason == 3):
        reason = "it isn't a valid URL (it doesn't begin with http:// or https://)."
        short_reason = "URL doesn't begin with http:// or https://"
    elif (reason == 4):
        reason = "it isn't a valid URL (it doesn't have a TLD such as .com)"
        short_reason = "URL doesn't have TLD (eg. .com, .co.uk)"
    else:
        reason = "we didn't feel like it (something happened at our end.)"
        short_reason = "didn't feel like it."
    # Return results.html template with requested variables
    if (is_valid_url == False):
        return Flask.render_template("invalid.html", url=the_url, the_reason=reason, the_short_reason=short_reason)
    else:
        return Flask.render_template("results.html", url=the_url, primary_domain=full_url.netloc, scheme=full_url.scheme, is_valid_url=is_valid_url, is_opinion=is_opinion)
# Database information
database_url = 'Wingo.mysql.pythonanywhere-services.com'
database_username = 'Wingo'
database_password = 'fakenewschecker'
