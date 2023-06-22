# IMDB-APIs
IMDB API Clone (JWT, Token, Throttling, Pagination, Testing)
<p>[Demo video]</p> "https://www.linkedin.com/feed/update/urn:li:activity:7068960484607033344/"

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
   
- **Watch List**
1. api/watch/list/
2. api/watch/\<int:movie_id>/
3. api/watch/list2/
 

- **Stream Platforms**
1. api/watch/stream/
2. api/watch/stream/<int:streamplatform_id>/


