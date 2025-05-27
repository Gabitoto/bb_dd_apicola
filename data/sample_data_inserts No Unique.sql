-- Datos de prueba para la base de datos apícola actualizada
-- Ejecutar después de crear las tablas

-- 1. Apicultores
INSERT INTO apicultor (nombre, apellido) VALUES
('Juan Carlos', 'Mendoza'),
('María Elena', 'Rodríguez'),
('Pedro Antonio', 'García'),
('Ana Sofía', 'López'),
('Miguel Ángel', 'Fernández');

-- 2. Analistas
INSERT INTO analista (nombres, apellidos, contacto) VALUES
('Dr. Carlos Alberto', 'Morales Vega', 'carlos.morales@lab.com'),
('Dra. Patricia', 'Silva Contreras', 'patricia.silva@lab.com'),
('Lic. Roberto', 'Jiménez Torres', 'roberto.jimenez@lab.com'),
('Ing. Laura', 'Hernández Ruiz', 'laura.hernandez@lab.com');

-- 3. Apiarios
INSERT INTO apiarios (id_apicultor, nombre_apiario, cant_colmenas, localidad, latitud, longitud) VALUES
(1, 'El Rosal', 25, 'Villa Mercedes', -33.67589, -65.45632),
(1, 'Las Flores', 18, 'San Luis Capital', -33.30154, -66.33569),
(2, 'Monte Verde', 32, 'Merlo', -32.34567, -65.01234),
(2, 'Cerro Azul', 22, 'Potrero de los Funes', -33.19876, -66.21345),
(3, 'La Colina', 28, 'Villa de la Quebrada', -32.98765, -65.67890),
(4, 'Praderas', 35, 'Juana Koslay', -33.12345, -66.45678),
(5, 'Alto Verde', 20, 'El Trapiche', -33.45678, -66.12345);

-- 4. Tambores
INSERT INTO tambor (num_registro) VALUES
('TB-2024-001'),
('TB-2024-002'),
('TB-2024-003'),
('TB-2024-004'),
('TB-2024-005'),
('TB-2024-006'),
('TB-2024-007'),
('TB-2024-008'),
('TB-2024-009'),
('TB-2024-010'),
('TB-2024-011'),
('TB-2024-012');

-- 5. Relación Tambor-Apiario
INSERT INTO tambor_api (id_tambor, id_apiario, fecha_asignacion) VALUES
(1, 1, '2024-01-15'),
(2, 1, '2024-01-15'),
(3, 2, '2024-01-20'),
(4, 2, '2024-01-20'),
(5, 3, '2024-02-01'),
(6, 3, '2024-02-01'),
(7, 4, '2024-02-10'),
(8, 5, '2024-02-15'),
(9, 6, '2024-03-01'),
(10, 6, '2024-03-01'),
(11, 7, '2024-03-10'),
(12, 7, '2024-03-10');

-- 6. Especies
INSERT INTO especies (nombre_cientifico, nombre_comun, familia) VALUES
('Eucalyptus globulus', 'Eucalipto común', 'Myrtaceae'),
('Acacia dealbata', 'Mimosa', 'Fabaceae'),
('Prosopis nigra', 'Algarrobo negro', 'Fabaceae'),
('Schinus molle', 'Aguaribay', 'Anacardiaceae'),
('Larrea divaricata', 'Jarilla', 'Zygophyllaceae'),
('Condalia microphylla', 'Piquillín', 'Rhamnaceae'),
('Geoffroea decorticans', 'Chañar', 'Fabaceae'),
('Bulnesia retama', 'Retamo', 'Zygophyllaceae'),
('Capparis atamisquea', 'Atamisque', 'Capparaceae'),
('Ziziphus mistol', 'Mistol', 'Rhamnaceae'),
('Cercidium praecox', 'Brea', 'Fabaceae'),
('Prosopis flexuosa', 'Algarrobo dulce', 'Fabaceae'),
('Aspidosperma quebracho-blanco', 'Quebracho blanco', 'Apocynaceae'),
('Lithraea molleoides', 'Molle de beber', 'Anacardiaceae');

-- 7. Muestras
INSERT INTO muestra (id_analista, fecha_extraccion, fecha_analisis, num_registro, observaciones) VALUES
(1, '2024-03-15', '2024-03-20', 'M-2024-001', 'Muestra de miel clara, aroma floral intenso'),
(1, '2024-03-18', '2024-03-25', 'M-2024-002', 'Miel oscura con cristalización parcial'),
(2, '2024-04-01', '2024-04-08', 'M-2024-003', 'Muestra homogénea, color ámbar'),
(2, '2024-04-05', '2024-04-12', 'M-2024-004', 'Presencia de cera, filtrada antes del análisis'),
(3, '2024-04-10', '2024-04-18', 'M-2024-005', 'Miel muy clara, posible origen de eucalipto'),
(3, '2024-04-15', NULL, 'M-2024-006', 'Muestra pendiente de análisis'),
(4, '2024-04-20', '2024-04-28', 'M-2024-007', 'Miel con aroma característico de algarrobo'),
(1, '2024-05-01', '2024-05-08', 'M-2024-008', 'Muestra multifloral típica de la región');

-- 8. Relación Muestra-Tambor
INSERT INTO muestra_tambor (id_muestra, id_tambor, fecha_asociacion) VALUES
(1, 1, '2024-03-15'),
(1, 2, '2024-03-15'),
(2, 3, '2024-03-18'),
(3, 4, '2024-04-01'),
(3, 5, '2024-04-01'),
(4, 6, '2024-04-05'),
(5, 7, '2024-04-10'),
(6, 8, '2024-04-15'),
(7, 9, '2024-04-20'),
(8, 10, '2024-05-01'),
(8, 11, '2024-05-01');

-- 9. Análisis Palinológico
INSERT INTO analisis_palinologico (id_muestra, id_especie, cantidad_granos, marca_especial, porcentaje) VALUES
-- Muestra 1: Predominio de Eucalipto
(1, 1, 450, NULL, 75.0),
(1, 2, 60, NULL, 10.0),
(1, 4, 45, NULL, 7.5),
(1, 6, 30, NULL, 5.0),
(1, 8, 15, NULL, 2.5),

-- Muestra 2: Mezcla de Algarrobos
(2, 3, 320, NULL, 45.0),
(2, 12, 240, NULL, 35.0),
(2, 7, 80, NULL, 12.0),
(2, 5, 40, NULL, 6.0),
(2, 9, 20, 'x', 2.0),

-- Muestra 3: Multifloral equilibrada
(3, 1, 180, NULL, 30.0),
(3, 3, 150, NULL, 25.0),
(3, 4, 120, NULL, 20.0),
(3, 2, 90, NULL, 15.0),
(3, 10, 60, NULL, 10.0),

-- Muestra 4: Predominio de Mimosa
(4, 2, 380, NULL, 65.0),
(4, 1, 100, NULL, 18.0),
(4, 6, 60, NULL, 10.0),
(4, 11, 30, NULL, 5.0),
(4, 13, 15, 'x', 2.0),

-- Muestra 5: Eucalipto puro
(5, 1, 520, NULL, 88.0),
(5, 2, 30, NULL, 5.0),
(5, 4, 25, NULL, 4.0),
(5, 8, 15, 'x', 2.5),
(5, 14, 5, 'x', 0.5),

-- Muestra 7: Algarrobo negro dominante
(7, 3, 400, NULL, 70.0),
(7, 12, 80, NULL, 15.0),
(7, 5, 50, NULL, 8.0),
(7, 7, 30, NULL, 5.0),
(7, 9, 15, 'x', 2.0),

-- Muestra 8: Multifloral compleja
(8, 1, 150, NULL, 25.0),
(8, 3, 120, NULL, 20.0),
(8, 2, 90, NULL, 15.0),
(8, 4, 75, NULL, 12.5),
(8, 6, 60, NULL, 10.0),
(8, 10, 45, NULL, 7.5),
(8, 11, 30, NULL, 5.0),
(8, 5, 24, NULL, 4.0),
(8, 14, 6, 'x', 1.0);