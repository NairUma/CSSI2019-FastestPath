import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#this function will set-up which map will be used.
def map_pick(location_one, location_two):
    if location_one == location_two:
        url = map0
    elif location_one == "Kellogg":
        if location_two == "USU":
            url = KellUSU
        if location_two == "Starbucks":
            url = KellStar
        if location_two == "SBSB":
            url = KellSBSB
        if location_two == "PS1":
            url = KellPS1
    elif location_one == "USU":
        if location_two == "Kellogg":
            url = KellUSU
        if location_two == "Starbucks":
            url = USUStar
        if location_two == "SBSB":
            url = USUSBSB
        if location_two == "PS1":
            url = USUPS1
    elif location_one == "Starbucks":
        if location_two == "Kellogg":
            url = KellStar
        if location_two == "USU":
            url = USUStar
        if location_two == "SBSB":
            url = StarSBSB
        if location_two == "PS1":
            url = StarPS1
    elif location_one == "SBSB":
        if location_two == "Kellogg":
            url = KellSBSB
        if location_two == "USU":
            url = USUSBSB
        if location_two == "Starbucks":
            url = StarSBSB
        if location_two == "PS1":
            url = SBSBPS1
    elif location_one == "PS1":
        if location_two == "Kellogg":
            url = KellPS1
        if location_two == "USU":
            url = USUPS1
        if location_two == "Starbucks":
            url = StarPS1
        if location_two == "SBSB":
            url = SBSBPS1
    else:
        self.response.write(main_template.render())
    return url
# this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('templates/index1.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(main_template.render())
# this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        insert html title where *** is
        end_template = the_jinja_env.get_template('templates/FastestPath.html')
        self.response.headers['Content-Type'] = 'html'
        map_url = map_pick(starting point, destination)
        the_variable_dict = {
            "img_url": "map_url"
        }
        self.response.write(end_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        location_one = self.request.get('starting point')
        location_two = self.request.get('destination')
        # correct_map = self.request.get('map')


        pic_url = get_meme_url(meme_img_choice)
        the_variable_dict = {"startpoint": user_loc1,
                             "endpoint": user_loc2,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/home', MainPage),
    ('/fastestpath', FastPage),

], debug=True)
