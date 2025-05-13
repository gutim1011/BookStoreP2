Proyecto BookStore - Aplicación Escalable
Introducción
BookStore es una aplicación web de ecommerce que permite a los usuarios publicar, comprar y vender libros de segunda mano. A diferencia de grandes plataformas de venta de libros nuevos, BookStore facilita un mercado distribuido entre usuarios. La aplicación fue desarrollada inicialmente como un monolito y posteriormente escalada y modernizada en la nube.

Objetivos del Proyecto
Objetivo 1: Despliegue Monolítico en AWS
•	Desplegar la aplicación BookStore en una instancia EC2 de AWS.
•	Configurar un dominio personalizado usando DuckDNS.
•	Instalar y configurar Nginx como proxy inverso.
•	Implementar HTTPS con Certbot y Let's Encrypt.
Objetivo 2: Escalamiento de la Aplicación Monolítica
•	Crear una AMI de la instancia configurada.
•	Implementar un Auto Scaling Group (ASG) con múltiples instancias EC2.
•	Balanceo de carga con Elastic Load Balancer (ELB).
•	Migración de la base de datos a Amazon RDS (MySQL).
•	Configuración de almacenamiento compartido usando Amazon EFS.
Objetivo 3: Reingeniería hacia Microservicios
•	Dividir la aplicación monolítica en tres microservicios:
o	Microservicio de Autenticación.
o	Microservicio de Catálogo.
o	Microservicio de Compras y Envíos.
•	Crear contenedores Docker individuales para cada microservicio.
•	Desplegar los microservicios en un clúster de Kubernetes (EKS).
•	Configurar escalabilidad independiente para cada microservicio.

Arquitectura General
•	Objetivo 1: Instancia EC2 │ Nginx │ Docker Compose (Flask + MySQL)
•	Objetivo 2:
o	Auto Scaling Group con múltiples EC2.
o	Elastic Load Balancer.
o	Base de datos separada en RDS.
o	Archivos compartidos en EFS.
•	Objetivo 3:
o	Clúster Kubernetes (EKS).
o	3 microservicios Dockerizados.
o	Ingress Controller para enrutamiento.
o	Base de datos persistente en RDS.
o	EFS como sistema de archivos compartido.

Tecnologías Utilizadas
•	AWS EC2, RDS, EFS, ELB, ASG, EKS
•	Docker, Docker Compose
•	Kubernetes (EKS)
•	Nginx
•	Let's Encrypt + Certbot
•	Flask (Backend)
•	MySQL (Base de Datos)
•	GitHub Actions (para CI/CD)

Instrucciones de Despliegue
Objetivo 1: Monolito en una VM
1.	Crear instancia EC2 Ubuntu 22.04 LTS.
2.	Instalar Docker, Docker Compose, Nginx y Certbot.
3.	Clonar el repositorio de BookStore.
4.	Ejecutar docker-compose up -d para levantar los servicios.
5.	Configurar Nginx como proxy inverso.
6.	Instalar certificado SSL con Certbot.
Objetivo 2: Escalamiento Monolítico
1.	Crear una AMI de la instancia.
2.	Configurar un Auto Scaling Group y Launch Template.
3.	Configurar Elastic Load Balancer.
4.	Crear base de datos en RDS y actualizar configuración.
5.	Crear sistema de archivos en EFS y montar en instancias.
6.	Actualizar DNS para apuntar al ELB.
Objetivo 3: Microservicios en Kubernetes
1.	Refactorizar código de BookStore en 3 microservicios.
2.	Crear Dockerfiles individuales.
3.	Subir imágenes a Amazon ECR.
4.	Desplegar microservicios en EKS.
5.	Configurar Ingress Controller para exponer servicios.
6.	Configurar autoescalado (HPA) por microservicio.

Resultados Alcanzados
•	Despliegue exitoso del monolito en EC2.
•	Escalamiento automático de instancias con ASG y balanceo de carga.
•	Alta disponibilidad de base de datos con Amazon RDS.
•	Migración a arquitectura de microservicios en clúster Kubernetes.
•	Dominio seguro accesible vía HTTPS.

Lecciones Aprendidas
•	Importancia de validar configuraciones antes de reiniciar servicios.
•	Correcta planificación de recursos en escalamiento vertical y horizontal.
•	Uso de buenas prácticas en Kubernetes para microservicios.
•	Automatización de despliegues reduce errores y tiempos.

Equipo
•	Esteban Giraldo Llano
•	Mariana Gutierrez Jaramillo
Diagrama:

https://lucid.app/lucidchart/a0dfcaf9-91a4-4cdb-8667-5c3415ebaaf8/edit?viewport_loc=-1030%2C-489%2C3174%2C1742%2C0_0&invitationId=inv_74990cf1-6783-4ac5-8ce3-42e300aad260

Dominio: https://proyecto2marianita.online/
