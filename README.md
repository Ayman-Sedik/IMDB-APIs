# IMDB APIs Project
IMDB API Clone (JWT, Token, Throttling, Pagination, Testing).
## [Demo video](https://drive.google.com/file/d/1sCEl6U557vOHQacd7SWz1FF-DWUDgxfr/view?usp=sharing)

## Concepts Applied
**1. API Basics**
   - Serializers {Serializers – ModelSerializer – HyperlinkedModelSerializer}

**2. Function-Based View**

**3. Class-Based Views**
   - {APIView – Generic View – Mixins – Concrete View Classes}

**4. Viewsets and Routers**

**5. Permissions**
   {IsAuthenticated – IsAdminUser – IsAuthenticatedOrReadOnly – Custom Permission}

**6. Authentications**
   {BasicAuthentication – TokenAuthentication – JSON Web Token Authentication}

**7. Throttling**
   - {AnonRateThrottle – UserRateThrottle – ScopedRate Throttle – Custom Throttles}

**8. Django Filter Backend**
   - {Filter – Search – Ordering}

**9. Pagination**
    - {Page Number – Limit Offset – Cursor}
  
**10. Automated API Testing**

## API URLs
**1. Admin Access**
   - /dashboard/
   
**2. Watch List**
   - api/watch/list/
   - api/watch/\<int:movie_id>/
   - api/watch/list2/ (Filter)
 
**3. Stream Platforms**
   - api/watch/stream/
   - api/watch/stream/\<int:streamplatform_id>/

**4. Reviews**
   - api/watch/\<int:movie_id>/reviews/ (All reviews for the movie)
   - api/watch/reviews/\<int:review_id>/ (Individual review)
   - api/watch/reviews/\<int:movie_id>/reviews/create/

**5. User Review**
   - api/watch/user-reviews/?username=example/ 

**6. Accounts**
   - api/account/register/
   - api/account/login/
   - api/account/logout/

