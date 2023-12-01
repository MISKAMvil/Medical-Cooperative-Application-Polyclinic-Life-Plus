-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Ноя 08 2023 г., 20:49
-- Версия сервера: 8.1.0
-- Версия PHP: 8.2.7


CREATE DATABASE mcaplpv1;
use mcaplpv1;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `mcaplpv1`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('bd941f5c8ef2');

-- --------------------------------------------------------

--
-- Структура таблицы `appointments`
--

CREATE TABLE `appointments` (
  `id` int NOT NULL,
  `patient_id` int NOT NULL,
  `date` datetime NOT NULL,
  `symptoms` varchar(255) NOT NULL,
  `diagnosis` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `appointments`
--

INSERT INTO `appointments` (`id`, `patient_id`, `date`, `symptoms`, `diagnosis`) VALUES
(1, 19, '2023-11-08 18:25:06', 'Кашель и боль в горле', 'Ангина'),
(2, 19, '2023-11-08 18:26:11', 'Кашель и боль в горле', 'Ангина'),
(3, 19, '2023-11-08 19:00:39', 'Насморк', 'Гайморит '),
(4, 19, '2023-11-08 19:06:20', 'Кашель и боль в горле', 'Гайморит '),
(5, 19, '2023-11-08 22:12:33', 'Кашель и боль в горле', 'Ангина'),
(6, 19, '2023-11-08 23:39:54', 'Насморк', 'Ангина'),
(7, 19, '2023-11-08 23:40:32', 'Насморк', 'Ангина'),
(8, 20, '2023-11-08 23:43:22', 'Насморк 2', 'Ангина 1');

-- --------------------------------------------------------

--
-- Структура таблицы `medications`
--

CREATE TABLE `medications` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `method_of_use` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `effects` text NOT NULL,
  `side_effects` text NOT NULL,
  `appointment_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `medications`
--

INSERT INTO `medications` (`id`, `name`, `method_of_use`, `description`, `effects`, `side_effects`, `appointment_id`) VALUES
(1, '123', '123', '123', '123', '123', NULL),
(2, '123', '213', '132', '312', '123', 7),
(3, 'qw qw', '1333', '1333', '1333', '3333', 8);

-- --------------------------------------------------------

--
-- Структура таблицы `patients`
--

CREATE TABLE `patients` (
  `id` int NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `birth_date` date NOT NULL,
  `home_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `patients`
--

INSERT INTO `patients` (`id`, `first_name`, `last_name`, `middle_name`, `gender`, `birth_date`, `home_address`) VALUES
(19, 'Максим', 'Балаев', 'Игоревич', 'Male', '2002-03-20', '12 Малая Семеновская'),
(20, 'Максим', 'Балаев', '', 'Male', '1922-02-02', 'дом 12');

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `name`, `desc`) VALUES
(1, 'Администратор', 'Суперпользователь, имеет полный доступ к системе.'),
(2, 'Пользователь', 'Учетная запись этого пользователя ограниченна в правах использования функционала приложения.');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `role_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password_hash`, `last_name`, `first_name`, `middle_name`, `role_id`) VALUES
(1, 'user1', 'pbkdf2:sha256:260000$tqJWXJnpa5rAasaR$bbb8e775aa0840a1a09161c7f99732c6dae5878fcdc5551f250308e4540ea022', 'Иванов', 'Иван', 'Иванович', 1),
(2, 'user2', 'pbkdf2:sha256:260000$NSNXsTypkIBdzIis$12a3cc9a9e90f8778f071fdd5f9661edc5653fe84130c110396c815307649a7f', 'Петров', 'Петр', 'Петрович', 2);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_appointments_patient_id_patients` (`patient_id`);

--
-- Индексы таблицы `medications`
--
ALTER TABLE `medications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_medications_appointment_id_appointments` (`appointment_id`);

--
-- Индексы таблицы `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_roles_name` (`name`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_users_login` (`login`),
  ADD KEY `fk_users_role_id_roles` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `appointments`
--
ALTER TABLE `appointments`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `medications`
--
ALTER TABLE `medications`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `appointments`
--
ALTER TABLE `appointments`
  ADD CONSTRAINT `fk_appointments_patient_id_patients` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`);

--
-- Ограничения внешнего ключа таблицы `medications`
--
ALTER TABLE `medications`
  ADD CONSTRAINT `fk_medications_appointment_id_appointments` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
