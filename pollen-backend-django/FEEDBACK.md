### PS: This is my very first time working with Django :-)
- I'm used to writing tests so the tests here took about 45minutes
- Also, you'll notice that in the test, I didn't assert some of the response of `recommendations/` (as I'd have done in a Flask app) mostly because the Response returns empty. I don't want to keep wasting time but I'll dig into this to understand how this works in Django.
- The part where I spent most time was in sending the rewards to the db. This is mostly because I was trying to use bulk_create to create the rewards and recommendation records. Had to go a different route and do them one-by-one which is hacky, but works for this purpose and saves time for now. Done is better than perfect.
- In total, I spent about 4 hours because it's my first experience with Django.

## Code Review `ticketing`
1. Remove duplicate code from setup_data.py.
```User.objects.create(
    id=1,
    name='John Doe',
    points=100,
    User.objects.create(
        id=2,
        name='Jane Doe',
        points=150,
    )
)```
We could use bulk_create since we already know the data we're parsing in. 
For example:
```
User.objects.bulk_create([
    User(id=1,name='John Doe',points=100),
    User(id=2,name='Jane Doe',points=150)
])
```
2. Check for non-existent data:
In the update endpoint, `def update_user(request):`, it would be great for us to check if the user exists and return the appropriate message before going ahead to update the user's points. This way, the API user doesn't get confused when they don't see an updated point for a non-existent user.

3. Redundant code:
`def getOrders(request, user_id):` seems to accepts a POST and PUT request but `request` paramer is not used. It should be removed and added at a later time when we're sure of what part of the order we want to allow update for.
Same goes for `def get_users(request):`
