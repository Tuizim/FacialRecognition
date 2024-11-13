from dataclasses import dataclass

@dataclass
class Credential:
    name: str
    cpf: str
    status: bool
    face: str
    def get_values(self) -> dict:
        return {
            "name": self.name,
            "cpf": self.cpf,
            "status": self.status,
            "face": self.face
        }