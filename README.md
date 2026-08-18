# projeto-mba-mlops

Projeto do curso de MLOps para ingestão, treino e entrega de um classificador.

## Estrutura

```
data/                 Dataset sintético de BOs (bos_sinteticos.csv)
terraform/            Infraestrutura como código (Terraform)
pulumi/               Infraestrutura como código (Pulumi)
airflow/dags/         Ingestão dos boletins
kubeflow/             Pipeline de treino do classificador
app/                  API, testes e Dockerfile
k8s/api/              Manifests Kubernetes
.github/workflows/    CI/CD
```

O arquivo `data/bos_sinteticos.csv` contém relatos fictícios para testes de classificação (`Furto`, `Roubo`, `Estelionato` e outras naturezas).
