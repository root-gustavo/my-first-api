import sqlite3
from fastapi import APIRouter, HTTPException, Depends
from src.api.models import User, UserCreate, UserUpdate
from config.path import DATABASE
from src.api.key import get_api_key

router = APIRouter(prefix="/api/v1")
DB_PATH = DATABASE / "database.db"


@router.get(
    "/users",
    response_model=list[User],
    summary="Listar todos os usuários",
    tags=["Usuários"],
    description=
    """
    Lista todos os usuários do sistema.
    """
)
def listar_usuarios(api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, telefone, sigla FROM users")
    rows = cursor.fetchall()
    conn.close()

    return [
        User(id=r[0], name=r[1], email=r[2], telefone=r[3], sigla=r[4])
        for r in rows
    ]


@router.get("/users/{user_id}", response_model=User)
def obter_usuario(user_id: int, api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, telefone, sigla FROM users WHERE id = ?", (user_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(404, "Usuário não encontrado")

    return User(id=row[0], name=row[1], email=row[2], telefone=row[3], sigla=row[4])


@router.post(
        "/users", 
        response_model=User,
        summary="Criar um usuario",
        tags=["Usuários"],
        description=
        """
        Pode criar qualquer usuario que você desejar
        """
        )
def criar_usuario(usuario: UserCreate, api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email, telefone, sigla)
        VALUES (?, ?, ?, ?)
        """,
        (usuario.name, usuario.email, usuario.telefone, usuario.sigla),
    )

    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return User(id=novo_id, **usuario.dict())


@router.put("/users/{user_id}", response_model=User)
def atualizar_usuario(user_id: int, usuario: UserCreate, api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(404, "Usuário não encontrado")

    cursor.execute(
        """
        UPDATE users
        SET name = ?, email = ?, telefone = ?, sigla = ?
        WHERE id = ?
        """,
        (usuario.name, usuario.email, usuario.telefone, usuario.sigla, user_id),
    )

    conn.commit()
    conn.close()

    return User(id=user_id, **usuario.dict())


@router.patch("/users/{user_id}", response_model=User)
def patch_usuario(user_id: int, usuario: UserUpdate, api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, telefone, sigla FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    if row is None:
        conn.close()
        raise HTTPException(404, "Usuário não encontrado")

    current = {
        "name": row[1],
        "email": row[2],
        "telefone": row[3],
        "sigla": row[4],
    }

    update_data = usuario.dict(exclude_unset=True)
    current.update(update_data)

    cursor.execute(
        """
        UPDATE users
        SET name = ?, email = ?, telefone = ?, sigla = ?
        WHERE id = ?
        """,
        (current["name"], current["email"], current["telefone"], current["sigla"], user_id),
    )

    conn.commit()
    conn.close()

    return User(id=user_id, **current)


@router.delete("/users/{user_id}")
def deletar_usuario(user_id: int, api_key: str = Depends(get_api_key)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(404, "Usuário não encontrado")

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    return {"message": "Usuário removido com sucesso"}
