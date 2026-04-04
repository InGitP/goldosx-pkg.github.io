from github import Github
import os

def cmd(args, path=None, gold=None):
    if len(args) < 3:
        print("uso: gpd upload <arquivo>")
        return

    if args[1] == "upload":
        file = args[2]

        if not os.path.exists(file):
            print("arquivo não existe")
            return

        if not file.endswith(".py"):
            print("só pode enviar .py")
            return

        token = "SEU_TOKEN_AQUI"  # depois tu pode melhorar isso

        g = Github(token)
        repo = g.get_repo("ingitp/goldosx-pkg.github.io")

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            # tenta atualizar se já existe
            contents = repo.get_contents(file)

            repo.update_file(
                path=file,
                message=f"update {file}",
                content=content,
                sha=contents.sha
            )
            print("pacote atualizado!")

        except:
            # senão, cria novo
            repo.create_file(
                path=file,
                message=f"add {file}",
                content=content
            )
            print("pacote enviado!")

        print("feito 🚀")
