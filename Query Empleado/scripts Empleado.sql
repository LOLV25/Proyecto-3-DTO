create database Empresa;
ALTER TABLE EMPLEADOS MODIFY COLUMN ID INT AUTO_INCREMENT;

select * from EMPLEADOS;
use Empresa;
create TABLE EMPLEADOS (
ID INTEGER ,
CEDULA VARCHAR(13) UNIQUE,
NOMBRE VARCHAR (100), 
APELLIDO VARCHAR(100),
SUELDO DECIMAL(10,2),
ESTADO VARCHAR(1),
USUARIO_CREACION INTEGER,
FECHA_CREACION DATETIME,
USUARIO_MODIFICACION INTEGER,
FECHA_MODIFICACION DATETIME,
PRIMARY KEY (ID)
)


  
