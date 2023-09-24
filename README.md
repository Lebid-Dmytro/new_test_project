###My test_app API for Inforce.

1. Build the Docker image on your computer - `docker-compose build`
2. Start the Docker - `docker-compose up`
3. Go to the API link - `http://127.0.0.1:8000/`
4. Check open documentation on this link - `http://127.0.0.1:8000/swagger/`

##Only registered users can interact with the site.

For Employee and Restaurant:
* `/api/v1/auth/users/` - Register
* `/api-auth/login/` - Login
* `/auth/token/login/` - User authentication with token

Restaurant:
* `/api/v1/restaurants/create/ `- Create new restaurant
* `/api/v1/restaurants/{restaurant_id}/menu/create/ `- Create new menu for restaurant
* `/api/v1/restaurant/` - Restaurants list
* `/api/v1/restaurant/{id}/` - View restaurant menu

Vote:
* `/api/v1/vote/create/` - Create new vote
* `/api/v1/vote/` - Votes list
* `/api/v1/favorite_menu/` - Today's winner


###Test.
Use - `docker-compose run web-app pytest`