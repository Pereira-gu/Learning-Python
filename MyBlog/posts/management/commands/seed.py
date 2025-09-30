from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post

class Command(BaseCommand):
    help = 'Semeia a base de dados com posts iniciais'
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('A iniciar o processo de seeding...'))

        # 1. Obter um utilizador para ser o autor dos posts
        # Vamos pegar o primeiro super-utilizador que existir.
        # Certifique-se de que já criou um com `python manage.py createsuperuser`
        try:
            author = User.objects.get(is_superuser=True)
            self.stdout.write(f'Utilizador autor encontrado: {author.username}')
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Nenhum super-utilizador encontrado. Por favor, crie um primeiro.'))
            return

        # 2. Dados dos posts a serem criados
        posts_data = [
            {
                "title": "5 Dicas Essenciais para Quem Está a Começar em Python",
                "content": """
Se está a dar os primeiros passos no mundo da programação com Python, seja bem-vindo! É uma linguagem poderosa e surpreendentemente fácil de aprender. Para te ajudar a começar com o pé direito, separei cinco dicas que fizeram toda a diferença para mim.

Primeiro, foque nos fundamentos. Não tenha pressa para pular para frameworks complexos como o Django ou para a ciência de dados. Gaste um bom tempo a entender variáveis, tipos de dados, loops (for, while) e condicionais (if, else). Uma base sólida tornará tudo mais fácil no futuro.

Segundo, pratique todos os dias. Mesmo que seja apenas por 15 ou 20 minutos. A consistência é mais importante do que a intensidade. Resolva pequenos desafios em sites como o HackerRank ou o LeetCode para exercitar a sua lógica.

Terceiro, leia o código de outras pessoas. Explore projetos open-source no GitHub. Tente entender como programadores mais experientes estruturam o seu código e resolvem problemas. Você aprenderá truques e boas práticas que não se encontram nos tutoriais.

Quarto, não tenha medo de errar. Os erros são os seus melhores professores. Cada mensagem de erro que você encontra e resolve é uma lição aprendida. Aprenda a usar o debugger e a pesquisar as suas dúvidas no Google ou no Stack Overflow.

Finalmente, construa algo! Pegue um conceito que aprendeu e crie um pequeno projeto pessoal. Pode ser uma calculadora, um jogo simples ou, como estamos a fazer, um blog! Colocar a mão na massa é a forma mais eficaz de solidificar o conhecimento.
                """
            },
            {
                "title": "A Arte de Fazer um Bom Café em Casa",
                "content": """
Para muitos, o café é o combustível que nos move durante o dia. Mas já parou para pensar na diferença entre um café "ok" e um café verdadeiramente incrível? A boa notícia é que não precisa de equipamentos caros para elevar a sua experiência de café em casa.

O segredo começa no grão. Dê preferência a grãos de café de origem única e moa-os na hora, se possível. A moagem liberta aromas que se perdem rapidamente, e o frescor faz uma diferença enorme no sabor final.

A água também é um ingrediente crucial. Use água filtrada e preste atenção à temperatura. A temperatura ideal para a extração do café é entre 90°C e 96°C. Água a ferver pode "queimar" o café, resultando num sabor amargo e desagradável.

Por último, explore diferentes métodos de preparo. A prensa francesa, o coador de papel (Hario V60) ou a Aeropress oferecem experiências sensoriais completamente diferentes. Cada método extrai sabores e aromas de formas únicas. Experimente e descubra qual deles agrada mais ao seu paladar. Fazer café pode ser um ritual relaxante e delicioso.
                """
            },
            {
                "title": "Como a Leitura de 20 Páginas por Dia Pode Mudar a Sua Vida",
                "content": """
Num mundo cheio de distrações digitais, o hábito da leitura parece estar a perder espaço. No entanto, o impacto de ler de forma consistente, mesmo que em pequenas doses, é profundo e transformador. O desafio é simples: ler 20 páginas de um livro, todos os dias.

No início, 20 páginas podem parecer pouco, mas a consistência é a chave. Ao final de um mês, você terá lido cerca de 600 páginas, o que equivale a dois ou três livros de tamanho médio. Em um ano, estamos a falar de mais de 25 livros! Imagine o conhecimento e as novas perspetivas que você pode adquirir.

A leitura expande o vocabulário, melhora a capacidade de concentração e estimula a criatividade. Ao mergulhar em diferentes histórias e assuntos, você exercita a sua empatia e a sua capacidade de pensar criticamente. Além disso, é uma excelente forma de reduzir o stress e relaxar antes de dormir, longe da luz azul dos ecrãs.

Escolha livros sobre assuntos que te interessem, sejam eles ficção, história, ciência ou biografias. O importante é criar o hábito e transformar a leitura numa parte indispensável do seu dia. Comece hoje!
                """
            }
        ]

        # 3. Criar os posts
        for post_data in posts_data:
            # Verifica se um post com o mesmo título já existe para não criar duplicados
            if not Post.objects.filter(title=post_data['title']).exists():
                Post.objects.create(
                    title=post_data['title'],
                    content=post_data['content'],
                    author=author
                )
                self.stdout.write(self.style.SUCCESS(f'Post "{post_data["title"]}" criado com sucesso.'))
            else:
                self.stdout.write(self.style.WARNING(f'Post "{post_data["title"]}" já existe. A ignorar.'))

        self.stdout.write(self.style.SUCCESS('Seeding concluído!'))