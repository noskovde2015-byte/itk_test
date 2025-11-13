from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.crud.crud import get_all_users, create_user, get_user_by_id, update_user, delete_user
from core.config import settings
from core.models import db_helper
from core.shemas.UserShema import UserRead, UserCreate, UserUpdate

router = APIRouter(prefix=settings.api.users, tags=["Users"])
@router.get(
    "",
    response_model=List[UserRead],
    summary="Get all users",
    description="""
    This endpoint returns all users
    
    Returns:
    - List of users
    
    Raises:
    - 500: Iternal Server Error
    """,
    responses={
        500: {
            "description": "Internal server error"
        }
    }
)
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    """Get all users router"""
    return await get_all_users(
        session=session,
    )


@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Get user by id",
    description="""
    Get one user by id
    
    Parameters:
    - User ID
    
    Returns:
    - User object
    
    Raises:
    - 404: User not found
    - 500: Internal Server Error""",


    responses = {
        404: {
            "description": "User not found"
        },
        500: {
            "description": "Internal server error"
        }
    }
)
async def get_user(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    """Get user by id"""
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return user

@router.post(
    "",
    response_model=UserRead,
    summary="Create a new user",

    description="""
    Create a new user in the system.

    Parameters:
    - name
    - surname
    - age
    - email

    Returns:
    - Created user object 

    Raises:
    - 400: Invalid input data
    - 422: Validation error
    - 500: Internal server error
    """,
    responses={
        500: {
            "description": "Internal server error",
        }
    }
)
async def create_new_user(
        user_create: UserCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    """Create a new user"""
    return await create_user(
        session=session,
        user_create=user_create
    )


@router.put(
    "/{user_id}",
    response_model=UserRead,
    summary="Update user",
    description="""
    Update user information

    Parameters:
    - user_id
    - name
    - surname
    - age
    - email

    Returns:
    - Updated user object

    Raises:
    - 404: User not found
    - 422: Validation error
    - 500: Internal server error
    """,
    responses={
        404: {
            "description": "User not found"
        },
        500: {
            "description": "Internal server error"
        }
    }
)
async def update_user_by_id(
        user_id: int,
        user_update: UserUpdate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    """Update user router"""
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return await update_user(
        session=session,
        user=user,
        user_update=user_update
    )


@router.delete(
    "/{user_id}",
    summary="Delete user",
    description="""
    Delete user from system

    Parameters:
    - user_id

    Returns:
    - message

    Raises:
    - 404: User not found
    - 500: Internal server error
    """,
    responses={

        404: {
            "description": "User not found"
        },
        500: {
            "description": "Internal server error"
        }
    }
)
async def delete_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    """Delete user router"""
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return await delete_user(
        session=session,
        user_id=user_id,
    )



