import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from models.todo import Todo
from shared.settings import settings  # Pydantic-based env loader

# Create async engine and session factory
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def read_todos():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Todo))
        todos = result.scalars().all()

    for todo in todos:
        status = "✅" if todo.completed else "❌"
        print(f"📝 {todo.id}: {todo.title} {status}")

if __name__ == "__main__":
    asyncio.run(read_todos())

