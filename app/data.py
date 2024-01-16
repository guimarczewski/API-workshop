from typing import List, Dict

class Produtos:
    # criar lista de produtos com str - chave - e any - valor, descricao, bool
    produtos: List[Dict[str, any]] = [

        {
            "id":1,
            "nome":"Smartphone",
            "descricao":"Um telefone inteligente",
            "preco":1500.00
        },
        {
            "id":2,
            "nome":"Notebook",
            "descricao":"Computador gamer",
            "preco":3500.00
        },
        {
            "id":3,
            "nome":"Tablet",
            "descricao":"Um computador movel",
            "preco":2500.00
        }
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id): # response
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status":404, "Mensagem":"Produto não encontrado"}