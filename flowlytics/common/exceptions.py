from fastapi import HTTPException


class NotFoundException(HTTPException):
  def __init__(self, **kwargs):
    super().__init__(status_code=404, **kwargs)


class ConflictException(HTTPException):
  def __init__(self, **kwargs):
    super().__init__(status_code=409, **kwargs)

