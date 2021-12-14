from config import *

class Pessoa(db.Model):
    # atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(254))

    # formato texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            "cpf: " + self.cpf + ", email: " + self.email

    # formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf
        }

class Disciplina(db.Model):
    # atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cargaHoraria = db.Column(db.Integer)
    ementa = db.Column(db.String(254))

    # formato texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            "carga horaria: " + str(self.cargaHoraria) + ", ementa: " + self.ementa

    # formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cargaHoraria": self.cargaHoraria,
            "ementa": self.ementa
        }

class EstudanteDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer)
    mediaFinal = db.Column(db.Integer)
    frequencia = db.Column(db.Integer)

    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False) 
    pessoa = db.relationship("Pessoa") 
    
    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False) 
    disciplina = db.relationship("Disciplina") 

    def __str__(self):
        return f"{self.semestre}, {self.pessoa}, {self.disciplina}, {self.mediaFinal}, {self.frequencia}"

    def json(self):
        return {
            "id":self.id,
            "semestre":self.semestre,
            "pessoa_id":self.pessoa_id,
            "pessoa":self.pessoa.json(),
            "disciplina_id":self.disciplina_id,
            "disciplina":self.disciplina.json(),
            "mediaFinal":self.mediaFinal,
            "frequencia":self.frequencia
        }


db.create_all()
# teste    
if __name__ == "__main__":
    p1 = Pessoa(
      id = 1,
      nome = "Teste 1",
      email = "email@email.com", 
      cpf = "12345678910"
      )

    p2 = Pessoa(
      id = 2,
      nome = "Teste 2",
      email = "email2@email.com", 
      cpf = "12345678911"
      )       
    
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1)
    print(p2)
    print(p1.json())
    print(p2.json())


  #Teste disciplina
    d1 = Disciplina(
      id = 1,
      nome = "Matematica",
      cargaHoraria = 10,
      ementa = "teste"
    )

    db.session.add(d1)
    print(d1)
    print(d1.json())

#Teste EstudanteDisciplina
    e1 = EstudanteDisciplina(
      id = 1,
      semestre = 1,
      pessoa_id= p1.id,
      pessoa = p1,
      disciplina_id = d1.id,
      disciplina = d1,
      mediaFinal = 10.10,
      frequencia = 75.10
    )

    db.session.add(e1)
    print(e1)
    print(e1.json())

    # drop da tabela 
    db.drop_all()