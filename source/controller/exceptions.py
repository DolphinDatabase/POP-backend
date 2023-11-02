from fastapi import HTTPException, status

registration_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Could not register user",
    headers={"WWW-Authenticate": "Bearer"},
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

role_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Role unauthorized",
    headers={"WWW-Authenticate": "Bearer"},
)

object_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Object not found",
    headers={"WWW-Authenticate": "Bearer"},
)

requires_accept_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="User need accept the Terms of Use",
    headers={"WWW-Authenticate": "Bearer"},
)

validation_error = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Verify payload",
    headers={"WWW-Authenticate": "Bearer"},
)
