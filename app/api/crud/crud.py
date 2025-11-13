from typing import Sequence

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.shemas.UserShema import UserCreate, UserUpdate


async def get_all_users(
        session: AsyncSession
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(
        user_id: int,
        session: AsyncSession,

):
    stmt = select(User).where(User.id == user_id)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user


async def create_user(
        user_create: UserCreate,
        session: AsyncSession
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_update: UserUpdate,
) -> User:
    update_data = user_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(
        session: AsyncSession,
        user_id: int,
):
    stmt = select(User).where(User.id == user_id)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    await session.delete(user)
    await session.commit()
    return {
        "message": "User deleted",
        "user_id": user_id,
    }
