-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-07-2024 a las 20:08:56
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `id` bigint(20) NOT NULL,
  `usuario_admin_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id`, `usuario_admin_id`) VALUES
(1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_interface_theme`
--

CREATE TABLE `admin_interface_theme` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `title` varchar(50) NOT NULL,
  `title_visible` tinyint(1) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `logo_visible` tinyint(1) NOT NULL,
  `css_header_background_color` varchar(10) NOT NULL,
  `title_color` varchar(10) NOT NULL,
  `css_header_text_color` varchar(10) NOT NULL,
  `css_header_link_color` varchar(10) NOT NULL,
  `css_header_link_hover_color` varchar(10) NOT NULL,
  `css_module_background_color` varchar(10) NOT NULL,
  `css_module_text_color` varchar(10) NOT NULL,
  `css_module_link_color` varchar(10) NOT NULL,
  `css_module_link_hover_color` varchar(10) NOT NULL,
  `css_module_rounded_corners` tinyint(1) NOT NULL,
  `css_generic_link_color` varchar(10) NOT NULL,
  `css_generic_link_hover_color` varchar(10) NOT NULL,
  `css_save_button_background_color` varchar(10) NOT NULL,
  `css_save_button_background_hover_color` varchar(10) NOT NULL,
  `css_save_button_text_color` varchar(10) NOT NULL,
  `css_delete_button_background_color` varchar(10) NOT NULL,
  `css_delete_button_background_hover_color` varchar(10) NOT NULL,
  `css_delete_button_text_color` varchar(10) NOT NULL,
  `list_filter_dropdown` tinyint(1) NOT NULL,
  `related_modal_active` tinyint(1) NOT NULL,
  `related_modal_background_color` varchar(10) NOT NULL,
  `related_modal_rounded_corners` tinyint(1) NOT NULL,
  `logo_color` varchar(10) NOT NULL,
  `recent_actions_visible` tinyint(1) NOT NULL,
  `favicon` varchar(100) NOT NULL,
  `related_modal_background_opacity` varchar(5) NOT NULL,
  `env_name` varchar(50) NOT NULL,
  `env_visible_in_header` tinyint(1) NOT NULL,
  `env_color` varchar(10) NOT NULL,
  `env_visible_in_favicon` tinyint(1) NOT NULL,
  `related_modal_close_button_visible` tinyint(1) NOT NULL,
  `language_chooser_active` tinyint(1) NOT NULL,
  `language_chooser_display` varchar(10) NOT NULL,
  `list_filter_sticky` tinyint(1) NOT NULL,
  `form_pagination_sticky` tinyint(1) NOT NULL,
  `form_submit_sticky` tinyint(1) NOT NULL,
  `css_module_background_selected_color` varchar(10) NOT NULL,
  `css_module_link_selected_color` varchar(10) NOT NULL,
  `logo_max_height` smallint(5) UNSIGNED NOT NULL CHECK (`logo_max_height` >= 0),
  `logo_max_width` smallint(5) UNSIGNED NOT NULL CHECK (`logo_max_width` >= 0),
  `foldable_apps` tinyint(1) NOT NULL,
  `language_chooser_control` varchar(20) NOT NULL,
  `list_filter_highlight` tinyint(1) NOT NULL,
  `list_filter_removal_links` tinyint(1) NOT NULL,
  `show_fieldsets_as_tabs` tinyint(1) NOT NULL,
  `show_inlines_as_tabs` tinyint(1) NOT NULL,
  `css_generic_link_active_color` varchar(10) NOT NULL,
  `collapsible_stacked_inlines` tinyint(1) NOT NULL,
  `collapsible_stacked_inlines_collapsed` tinyint(1) NOT NULL,
  `collapsible_tabular_inlines` tinyint(1) NOT NULL,
  `collapsible_tabular_inlines_collapsed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `admin_interface_theme`
--

INSERT INTO `admin_interface_theme` (`id`, `name`, `active`, `title`, `title_visible`, `logo`, `logo_visible`, `css_header_background_color`, `title_color`, `css_header_text_color`, `css_header_link_color`, `css_header_link_hover_color`, `css_module_background_color`, `css_module_text_color`, `css_module_link_color`, `css_module_link_hover_color`, `css_module_rounded_corners`, `css_generic_link_color`, `css_generic_link_hover_color`, `css_save_button_background_color`, `css_save_button_background_hover_color`, `css_save_button_text_color`, `css_delete_button_background_color`, `css_delete_button_background_hover_color`, `css_delete_button_text_color`, `list_filter_dropdown`, `related_modal_active`, `related_modal_background_color`, `related_modal_rounded_corners`, `logo_color`, `recent_actions_visible`, `favicon`, `related_modal_background_opacity`, `env_name`, `env_visible_in_header`, `env_color`, `env_visible_in_favicon`, `related_modal_close_button_visible`, `language_chooser_active`, `language_chooser_display`, `list_filter_sticky`, `form_pagination_sticky`, `form_submit_sticky`, `css_module_background_selected_color`, `css_module_link_selected_color`, `logo_max_height`, `logo_max_width`, `foldable_apps`, `language_chooser_control`, `list_filter_highlight`, `list_filter_removal_links`, `show_fieldsets_as_tabs`, `show_inlines_as_tabs`, `css_generic_link_active_color`, `collapsible_stacked_inlines`, `collapsible_stacked_inlines_collapsed`, `collapsible_tabular_inlines`, `collapsible_tabular_inlines_collapsed`) VALUES
(1, 'Django', 1, 'Administración de Django', 1, '', 1, '#0C4B33', '#F5DD5D', '#44B78B', '#FFFFFF', '#C9F0DD', '#44B78B', '#FFFFFF', '#FFFFFF', '#C9F0DD', 1, '#0C3C26', '#156641', '#0C4B33', '#0C3C26', '#FFFFFF', '#BA2121', '#A41515', '#FFFFFF', 1, 1, '#000000', 1, '#FFFFFF', 1, '', '0.3', '', 1, '#E74C3C', 1, 1, 1, 'code', 1, 0, 0, '#FFFFCC', '#FFFFFF', 100, 400, 1, 'default-select', 1, 0, 0, 0, '#29B864', 0, 1, 0, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add Theme', 1, 'add_theme'),
(2, 'Can change Theme', 1, 'change_theme'),
(3, 'Can delete Theme', 1, 'delete_theme'),
(4, 'Can view Theme', 1, 'view_theme'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Proveedor', 7, 'add_proveedor'),
(26, 'Can change Proveedor', 7, 'change_proveedor'),
(27, 'Can delete Proveedor', 7, 'delete_proveedor'),
(28, 'Can view Proveedor', 7, 'view_proveedor'),
(29, 'Can add Rol', 8, 'add_rol'),
(30, 'Can change Rol', 8, 'change_rol'),
(31, 'Can delete Rol', 8, 'delete_rol'),
(32, 'Can view Rol', 8, 'view_rol'),
(33, 'Can add Usuario Personalizado', 9, 'add_usuario'),
(34, 'Can change Usuario Personalizado', 9, 'change_usuario'),
(35, 'Can delete Usuario Personalizado', 9, 'delete_usuario'),
(36, 'Can view Usuario Personalizado', 9, 'view_usuario'),
(37, 'Can add Administrador', 10, 'add_administrador'),
(38, 'Can change Administrador', 10, 'change_administrador'),
(39, 'Can delete Administrador', 10, 'delete_administrador'),
(40, 'Can view Administrador', 10, 'view_administrador'),
(41, 'Can add Cliente', 11, 'add_cliente'),
(42, 'Can change Cliente', 11, 'change_cliente'),
(43, 'Can delete Cliente', 11, 'delete_cliente'),
(44, 'Can view Cliente', 11, 'view_cliente'),
(45, 'Can add Empleado', 12, 'add_empleado'),
(46, 'Can change Empleado', 12, 'change_empleado'),
(47, 'Can delete Empleado', 12, 'delete_empleado'),
(48, 'Can view Empleado', 12, 'view_empleado'),
(49, 'Can add Rol Usuario', 13, 'add_rolusuario'),
(50, 'Can change Rol Usuario', 13, 'change_rolusuario'),
(51, 'Can delete Rol Usuario', 13, 'delete_rolusuario'),
(52, 'Can view Rol Usuario', 13, 'view_rolusuario'),
(53, 'Can add Materia prima', 14, 'add_materia_prima'),
(54, 'Can change Materia prima', 14, 'change_materia_prima'),
(55, 'Can delete Materia prima', 14, 'delete_materia_prima'),
(56, 'Can view Materia prima', 14, 'view_materia_prima'),
(57, 'Can add producto', 15, 'add_productos'),
(58, 'Can change producto', 15, 'change_productos'),
(59, 'Can delete producto', 15, 'delete_productos'),
(60, 'Can view producto', 15, 'view_productos'),
(61, 'Can add orden produccion', 16, 'add_orden_produccion'),
(62, 'Can change orden produccion', 16, 'change_orden_produccion'),
(63, 'Can delete orden produccion', 16, 'delete_orden_produccion'),
(64, 'Can view orden produccion', 16, 'view_orden_produccion'),
(65, 'Can add Calificación Producto', 17, 'add_calificacion_producto'),
(66, 'Can change Calificación Producto', 17, 'change_calificacion_producto'),
(67, 'Can delete Calificación Producto', 17, 'delete_calificacion_producto'),
(68, 'Can view Calificación Producto', 17, 'view_calificacion_producto'),
(69, 'Can add Factura', 18, 'add_factura'),
(70, 'Can change Factura', 18, 'change_factura'),
(71, 'Can delete Factura', 18, 'delete_factura'),
(72, 'Can view Factura', 18, 'view_factura'),
(73, 'Can add Factura de compra', 19, 'add_factura_compra'),
(74, 'Can change Factura de compra', 19, 'change_factura_compra'),
(75, 'Can delete Factura de compra', 19, 'delete_factura_compra'),
(76, 'Can view Factura de compra', 19, 'view_factura_compra'),
(77, 'Can add Factura Producto', 20, 'add_factura_producto'),
(78, 'Can change Factura Producto', 20, 'change_factura_producto'),
(79, 'Can delete Factura Producto', 20, 'delete_factura_producto'),
(80, 'Can view Factura Producto', 20, 'view_factura_producto'),
(81, 'Can add Factura venta', 21, 'add_factura_venta'),
(82, 'Can change Factura venta', 21, 'change_factura_venta'),
(83, 'Can delete Factura venta', 21, 'delete_factura_venta'),
(84, 'Can view Factura venta', 21, 'view_factura_venta'),
(85, 'Can add pedido', 22, 'add_pedido'),
(86, 'Can change pedido', 22, 'change_pedido'),
(87, 'Can delete pedido', 22, 'delete_pedido'),
(88, 'Can view pedido', 22, 'view_pedido'),
(89, 'Can add producto', 23, 'add_producto'),
(90, 'Can change producto', 23, 'change_producto'),
(91, 'Can delete producto', 23, 'delete_producto'),
(92, 'Can view producto', 23, 'view_producto'),
(93, 'Can add carrito', 24, 'add_carrito'),
(94, 'Can change carrito', 24, 'change_carrito'),
(95, 'Can delete carrito', 24, 'delete_carrito'),
(96, 'Can view carrito', 24, 'view_carrito'),
(97, 'Can add item carrito', 25, 'add_itemcarrito'),
(98, 'Can change item carrito', 25, 'change_itemcarrito'),
(99, 'Can delete item carrito', 25, 'delete_itemcarrito'),
(100, 'Can view item carrito', 25, 'view_itemcarrito'),
(101, 'Can add producto', 15, 'add_producto'),
(102, 'Can change producto', 15, 'change_producto'),
(103, 'Can delete producto', 15, 'delete_producto'),
(104, 'Can view producto', 15, 'view_producto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacion_producto`
--

CREATE TABLE `calificacion_producto` (
  `id` bigint(20) NOT NULL,
  `valor_calificacion` int(11) NOT NULL,
  `des_calificacion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificacion_producto`
--

INSERT INTO `calificacion_producto` (`id`, `valor_calificacion`, `des_calificacion`) VALUES
(1, 4, 'muy bueno pero algo frio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` bigint(20) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `fecha_nacimiento`, `usuario_id`) VALUES
(3, '2024-03-12', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-03-31 02:38:40.045934', '1', 'ya basta', 1, '[{\"added\": {}}]', 18, 3),
(2, '2024-03-31 02:56:32.488285', '1', 'ya basta', 2, '[]', 18, 3),
(3, '2024-03-31 02:57:28.151295', '2', 'alto policia', 1, '[{\"added\": {}}]', 18, 3),
(4, '2024-03-31 22:35:29.002839', '7', 'factura 4', 3, '', 18, 3),
(5, '2024-03-31 22:35:29.004839', '8', 'factura 4', 3, '', 18, 3),
(6, '2024-03-31 22:35:29.006839', '9', 'factura 4', 3, '', 18, 3),
(7, '2024-03-31 22:35:29.009839', '10', 'factura 4', 3, '', 18, 3),
(8, '2024-04-04 19:22:56.235710', '31', 'factura 2', 2, '[{\"changed\": {\"fields\": [\"Iva\"]}}]', 18, 3),
(9, '2024-04-04 21:38:21.267764', '1', 'ya basta', 1, '[{\"added\": {}}]', 15, 3),
(10, '2024-04-04 22:03:59.896748', '2', 'alto policia', 2, '[]', 18, 3),
(11, '2024-04-04 22:05:19.245665', '2', 'alto policia', 2, '[]', 18, 3),
(12, '2024-04-05 02:17:55.609277', '35', 'no mamessssssssssss', 3, '', 18, 3),
(13, '2024-04-09 20:41:48.084383', '2', 'queso chocolate', 1, '[{\"added\": {}}]', 15, 3),
(14, '2024-04-09 20:42:32.350035', '3', 'wuatafak', 1, '[{\"added\": {}}]', 15, 3),
(15, '2024-04-09 20:52:38.205809', '1', 'ya basta', 3, '', 15, 3),
(16, '2024-04-09 20:52:38.207818', '2', 'queso chocolate', 3, '', 15, 3),
(17, '2024-04-09 20:52:38.209813', '3', 'wuatafak', 3, '', 15, 3),
(18, '2024-04-09 20:55:31.609968', '4', 'Queso Pera', 1, '[{\"added\": {}}]', 15, 3),
(19, '2024-04-09 21:06:35.551014', '4', 'Queso Pera', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 15, 3),
(20, '2024-04-09 22:57:09.869535', '4', 'Queso Pera', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 15, 3),
(21, '2024-04-09 23:04:13.313805', '9', 'Arepa quesuda', 3, '', 15, 3),
(22, '2024-04-10 00:13:56.630282', '4', 'juanito_alcachofa@gmail.com', 3, '', 9, 3),
(23, '2024-06-28 19:45:29.613738', '1', 'leche', 1, '[{\"added\": {}}]', 14, 3),
(24, '2024-06-28 19:46:14.284859', '2', 'suero', 1, '[{\"added\": {}}]', 14, 3),
(25, '2024-06-28 19:46:17.530000', '2', 'suero', 2, '[]', 14, 3),
(26, '2024-06-28 19:48:54.852704', '1', 'parmalat', 1, '[{\"added\": {}}]', 7, 3),
(27, '2024-06-28 19:49:09.672828', '2', 'alqueria', 1, '[{\"added\": {}}]', 7, 3),
(28, '2024-06-28 21:07:37.328626', '4', 'Orden #4 - Producto: queso arequipe - Cantidad: 12', 1, '[{\"added\": {}}]', 16, 3),
(29, '2024-06-28 21:08:23.791308', '1', '4', 1, '[{\"added\": {}}]', 17, 3),
(30, '2024-06-28 21:11:38.374068', '1', 'Factura Producto - Cantidad: 12 - Producto: Queso Bocadillo ', 1, '[{\"added\": {}}]', 20, 3),
(31, '2024-06-28 21:15:37.191040', '3', 'juanito_alcachofa@gmail.com', 1, '[{\"added\": {}}]', 11, 3),
(32, '2024-06-28 21:17:40.161905', '2', 'example@gmail.com', 1, '[{\"added\": {}}]', 12, 3),
(33, '2024-06-30 23:23:01.391138', '2', 'Factura Compra - Proveedor: parmalat - Empleado: example@gmail.com', 1, '[{\"added\": {}}]', 19, 3),
(34, '2024-06-30 23:23:21.463598', '1', 'Factura Venta - Empleado: example@gmail.com - Cliente: juanito_alcachofa@gmail.com', 1, '[{\"added\": {}}]', 21, 3),
(35, '2024-06-30 23:24:43.325955', '1', 'jadu.jair@gmail.com', 1, '[{\"added\": {}}]', 10, 3),
(36, '2024-06-30 23:25:53.973327', '1', 'administrador', 1, '[{\"added\": {}}]', 8, 3),
(37, '2024-06-30 23:26:05.794625', '1', 'jadu.jair@gmail.com - administrador', 1, '[{\"added\": {}}]', 13, 3),
(38, '2024-07-01 01:37:49.174752', '7', 'example2@gmail.com', 1, '[{\"added\": {}}]', 9, 3),
(39, '2024-07-01 01:38:10.130319', '3', 'example2@gmail.com', 1, '[{\"added\": {}}]', 12, 3),
(40, '2024-07-01 01:38:56.879458', '2', 'Factura Venta - Empleado: example2@gmail.com - Cliente: juanito_alcachofa@gmail.com', 1, '[{\"added\": {}}]', 21, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(1, 'admin_interface', 'theme'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'contenttypes', 'contenttype'),
(14, 'inventory', 'materia_prima'),
(16, 'inventory', 'orden_produccion'),
(15, 'inventory', 'producto'),
(17, 'sales', 'calificacion_producto'),
(18, 'sales', 'factura'),
(19, 'sales', 'factura_compra'),
(20, 'sales', 'factura_producto'),
(21, 'sales', 'factura_venta'),
(6, 'sessions', 'session'),
(24, 'shopping_cart', 'carrito'),
(25, 'shopping_cart', 'itemcarrito'),
(22, 'shopping_cart', 'pedido'),
(23, 'shopping_cart', 'producto'),
(10, 'user_app', 'administrador'),
(11, 'user_app', 'cliente'),
(12, 'user_app', 'empleado'),
(7, 'user_app', 'proveedor'),
(8, 'user_app', 'rol'),
(13, 'user_app', 'rolusuario'),
(9, 'user_app', 'usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-30 18:14:44.383489'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-03-30 18:14:44.418550'),
(3, 'auth', '0001_initial', '2024-03-30 18:14:44.534350'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-03-30 18:14:44.561238'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-03-30 18:14:44.565239'),
(6, 'auth', '0004_alter_user_username_opts', '2024-03-30 18:14:44.568240'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-03-30 18:14:44.572241'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-03-30 18:14:44.573164'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-03-30 18:14:44.576166'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-03-30 18:14:44.579166'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-03-30 18:14:44.583168'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-03-30 18:14:44.589169'),
(13, 'auth', '0011_update_proxy_permissions', '2024-03-30 18:14:44.593169'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-03-30 18:14:44.598171'),
(15, 'user_app', '0001_initial', '2024-03-30 18:14:44.893226'),
(16, 'admin', '0001_initial', '2024-03-30 18:14:44.952245'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-03-30 18:14:44.959246'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-30 18:14:44.967248'),
(19, 'admin_interface', '0001_initial', '2024-03-30 18:14:44.974249'),
(20, 'admin_interface', '0002_add_related_modal', '2024-03-30 18:14:45.002226'),
(21, 'admin_interface', '0003_add_logo_color', '2024-03-30 18:14:45.011228'),
(22, 'admin_interface', '0004_rename_title_color', '2024-03-30 18:14:45.017230'),
(23, 'admin_interface', '0005_add_recent_actions_visible', '2024-03-30 18:14:45.025231'),
(24, 'admin_interface', '0006_bytes_to_str', '2024-03-30 18:14:45.064240'),
(25, 'admin_interface', '0007_add_favicon', '2024-03-30 18:14:45.075890'),
(26, 'admin_interface', '0008_change_related_modal_background_opacity_type', '2024-03-30 18:14:45.092894'),
(27, 'admin_interface', '0009_add_enviroment', '2024-03-30 18:14:45.112901'),
(28, 'admin_interface', '0010_add_localization', '2024-03-30 18:14:45.124904'),
(29, 'admin_interface', '0011_add_environment_options', '2024-03-30 18:14:45.151910'),
(30, 'admin_interface', '0012_update_verbose_names', '2024-03-30 18:14:45.155911'),
(31, 'admin_interface', '0013_add_related_modal_close_button', '2024-03-30 18:14:45.163907'),
(32, 'admin_interface', '0014_name_unique', '2024-03-30 18:14:45.171908'),
(33, 'admin_interface', '0015_add_language_chooser_active', '2024-03-30 18:14:45.180911'),
(34, 'admin_interface', '0016_add_language_chooser_display', '2024-03-30 18:14:45.187912'),
(35, 'admin_interface', '0017_change_list_filter_dropdown', '2024-03-30 18:14:45.192349'),
(36, 'admin_interface', '0018_theme_list_filter_sticky', '2024-03-30 18:14:45.199908'),
(37, 'admin_interface', '0019_add_form_sticky', '2024-03-30 18:14:45.214911'),
(38, 'admin_interface', '0020_module_selected_colors', '2024-03-30 18:14:45.238917'),
(39, 'admin_interface', '0021_file_extension_validator', '2024-03-30 18:14:45.243918'),
(40, 'admin_interface', '0022_add_logo_max_width_and_height', '2024-03-30 18:14:45.259925'),
(41, 'admin_interface', '0023_theme_foldable_apps', '2024-03-30 18:14:45.267926'),
(42, 'admin_interface', '0024_remove_theme_css', '2024-03-30 18:14:45.274929'),
(43, 'admin_interface', '0025_theme_language_chooser_control', '2024-03-30 18:14:45.282930'),
(44, 'admin_interface', '0026_theme_list_filter_highlight', '2024-03-30 18:14:45.291889'),
(45, 'admin_interface', '0027_theme_list_filter_removal_links', '2024-03-30 18:14:45.300891'),
(46, 'admin_interface', '0028_theme_show_fieldsets_as_tabs_and_more', '2024-03-30 18:14:45.316695'),
(47, 'admin_interface', '0029_theme_css_generic_link_active_color', '2024-03-30 18:14:45.324699'),
(48, 'admin_interface', '0030_theme_collapsible_stacked_inlines_and_more', '2024-03-30 18:14:45.355707'),
(49, 'inventory', '0001_initial', '2024-03-30 18:14:45.426230'),
(50, 'sales', '0001_initial', '2024-03-30 18:14:45.456238'),
(51, 'sales', '0002_initial', '2024-03-30 18:14:45.663166'),
(52, 'sessions', '0001_initial', '2024-03-30 18:14:45.676168'),
(53, 'user_app', '0002_alter_usuario_table', '2024-03-30 18:14:45.695173'),
(54, 'user_app', '0003_alter_usuario_managers_remove_usuario_date_joined_and_more', '2024-03-30 18:14:45.800353'),
(55, 'user_app', '0004_alter_usuario_segundo_apellido_and_more', '2024-03-30 18:14:45.847364'),
(56, 'shopping_cart', '0001_initial', '2024-04-08 22:46:32.137072'),
(57, 'sales', '0003_alter_factura_name', '2024-04-09 20:40:07.568379'),
(58, 'shopping_cart', '0002_alter_itemcarrito_producto_delete_producto', '2024-04-09 20:40:08.609097'),
(59, 'inventory', '0002_productos_imagen', '2024-04-09 20:49:52.811319'),
(60, 'inventory', '0003_rename_productos_producto', '2024-04-09 21:24:51.140491'),
(61, 'inventory', '0004_alter_producto_valor', '2024-04-09 22:12:35.949670'),
(62, 'sales', '0004_alter_factura_iva_alter_factura_subtotal_and_more', '2024-06-14 18:28:34.698833'),
(63, 'inventory', '0005_alter_orden_produccion_options_and_more', '2024-06-28 21:05:57.951202'),
(64, 'sales', '0005_alter_calificacion_producto_table_and_more', '2024-06-28 21:05:57.999212'),
(65, 'sales', '0006_alter_factura_producto_valor_productos', '2024-06-28 21:10:44.715441'),
(66, 'user_app', '0005_alter_empleado_sueldo', '2024-06-28 21:16:44.336860'),
(67, 'inventory', '0006_rename_name_producto_nombre', '2024-06-28 21:41:16.144505');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('615pfia7wuwmxyeqiupkna6uexulxm61', '.eJxVjMEOwiAQRP-FsyEskBU8evcbyAKLVA0kpT0Z_9026UFPk8x7M28RaF1qWAfPYcriIlCcfrtI6cltB_lB7d5l6m2Zpyh3RR50yFvP_Loe7t9BpVG3tVHJF7QGfMm0JYLis0WH7IhRM0BC0oCRs1XAVlEmpQ17510BzeLzBc70N28:1sNl1H:7240Smtb5hXElKZilcuvz6l_HnjlgMi0CfOOnJ1kAdo', '2024-07-14 03:14:27.597444'),
('qr1zn5g4rk6jcc909aktnoa7w0n2feyj', '.eJxVjMsOwiAQRf-FtSFQHgMu3fcbyMyAUjU0Ke3K-O_apAvd3nPOfYmE21rT1suSpizOwojT70bIj9J2kO_YbrPkua3LRHJX5EG7HOdcnpfD_Tuo2Ou3jgpIG-fBWo7IwVgFBQYVWGFUBlBTYCBv2V_J68wBCnsayDrns83i_QG_ZTd2:1ruM0e:10uAUZ0APRuJueflGa794EYoS_UnFbicxm4-autilsA', '2024-04-24 00:40:16.063662'),
('vt0op9demc2tryuwrzn84lxivc1mmcmf', '.eJxVjMsOwiAQRf-FtSFQHgMu3fcbyMyAUjU0Ke3K-O_apAvd3nPOfYmE21rT1suSpizOwojT70bIj9J2kO_YbrPkua3LRHJX5EG7HOdcnpfD_Tuo2Ou3jgpIG-fBWo7IwVgFBQYVWGFUBlBTYCBv2V_J68wBCnsayDrns83i_QG_ZTd2:1sOLBo:LFaGLjNNiSvMy0TLr67UEDFTvzubJkWXHypEo4gQcoU', '2024-07-15 17:51:44.228699');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` bigint(20) NOT NULL,
  `sueldo` decimal(10,2) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `sueldo`, `usuario_id`) VALUES
(2, 120000.00, 6),
(3, 21313.00, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `fecha_factura` datetime(6) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura`
--

INSERT INTO `factura` (`id`, `name`, `fecha_factura`, `subtotal`, `iva`, `total`) VALUES
(42, 'Queso Pera', '2024-06-14 18:29:00.000000', 20000.30, 7000.00, 27000.30),
(43, 'Factuar 2', '2024-06-20 19:41:00.000000', 12311.00, 3122.00, 23442.00),
(44, 'queso chocolate', '2024-06-28 19:39:00.000000', 10000.00, 2000.00, 12000.00),
(45, 'factura 4', '2024-07-01 17:51:00.000000', 34243.00, 5345.00, 32445.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_compra`
--

CREATE TABLE `factura_compra` (
  `id` bigint(20) NOT NULL,
  `empleados_id` bigint(20) NOT NULL,
  `proveedores_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura_compra`
--

INSERT INTO `factura_compra` (`id`, `empleados_id`, `proveedores_id`) VALUES
(2, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_producto`
--

CREATE TABLE `factura_producto` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `valor_productos` decimal(10,2) NOT NULL,
  `calificacion_producto_id` bigint(20) NOT NULL,
  `factura_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura_producto`
--

INSERT INTO `factura_producto` (`id`, `cantidad`, `valor_productos`, `calificacion_producto_id`, `factura_id`, `producto_id`) VALUES
(1, 12, 12000.00, 1, 43, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_venta`
--

CREATE TABLE `factura_venta` (
  `id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `empleados_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura_venta`
--

INSERT INTO `factura_venta` (`id`, `cliente_id`, `empleados_id`) VALUES
(1, 3, 2),
(2, 3, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia_prima`
--

CREATE TABLE `materia_prima` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_venta` date NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materia_prima`
--

INSERT INTO `materia_prima` (`id`, `name`, `descripcion`, `fecha_venta`, `cantidad`) VALUES
(1, 'leche', 'leche fresca de vaca', '2024-06-28', 199),
(2, 'suero', 'suero para quesos', '2023-06-28', 66);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden_produccion`
--

CREATE TABLE `orden_produccion` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `cantidad_materia_utilizada` int(11) NOT NULL,
  `fecha_orden` date NOT NULL,
  `materia_prima_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `orden_produccion`
--

INSERT INTO `orden_produccion` (`id`, `cantidad`, `cantidad_materia_utilizada`, `fecha_orden`, `materia_prima_id`, `producto_id`) VALUES
(4, 12, 23, '2024-06-28', 1, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `cantidad_existente` int(11) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `descripcion`, `valor`, `fecha_vencimiento`, `cantidad_existente`, `imagen`) VALUES
(4, 'Queso Pera', 'Queso pera relleno de chocolate', 400.00, '2024-04-09', 10, 'productos/chocoqueso.png'),
(10, 'Queso cocholate', 'queso postre', 12000.00, '2024-06-28', 12, 'productos/chocoqueso_2oT1eFD.png'),
(12, 'queso arequipe', 'Queso pera relleno', 12000.00, '2024-06-28', 12, 'productos/538b3fa9-ecd7-4766-94a2-1fb0114552f7.jfif');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `numero_telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id`, `nombre`, `direccion`, `numero_telefono`) VALUES
(1, 'parmalat', 'calle 52 g sur 27-22', 23423432),
(2, 'alqueria', 'calle 3 g sur 21-2', 34234566);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`, `estado`) VALUES
(1, 'administrador', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles_usuarios`
--

CREATE TABLE `roles_usuarios` (
  `id` bigint(20) NOT NULL,
  `rol_id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles_usuarios`
--

INSERT INTO `roles_usuarios` (`id`, `rol_id`, `usuario_id`) VALUES
(1, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shopping_cart_carrito`
--

CREATE TABLE `shopping_cart_carrito` (
  `id` bigint(20) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shopping_cart_itemcarrito`
--

CREATE TABLE `shopping_cart_itemcarrito` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shopping_cart_pedido`
--

CREATE TABLE `shopping_cart_pedido` (
  `id` bigint(20) NOT NULL,
  `direccion_envio` longtext NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shopping_cart_pedido_items`
--

CREATE TABLE `shopping_cart_pedido_items` (
  `id` bigint(20) NOT NULL,
  `pedido_id` bigint(20) NOT NULL,
  `itemcarrito_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_app_usuario`
--

CREATE TABLE `user_app_usuario` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `documento` int(11) NOT NULL,
  `primer_nombre` varchar(200) NOT NULL,
  `segundo_nombre` varchar(200) DEFAULT NULL,
  `primer_apellido` varchar(200) NOT NULL,
  `segundo_apellido` varchar(200) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user_app_usuario`
--

INSERT INTO `user_app_usuario` (`id`, `password`, `last_login`, `is_staff`, `is_active`, `documento`, `primer_nombre`, `segundo_nombre`, `primer_apellido`, `segundo_apellido`, `telefono`, `email`) VALUES
(3, 'pbkdf2_sha256$720000$fifzGoBfbOYybAp56UwI7y$NOZ26xyivPNDdWBkjxIgPUov3sPB7RWC7ewCRSciEvA=', '2024-07-01 17:51:44.226699', 1, 1, 1001282605, 'jair', NULL, 'perez', NULL, NULL, 'jadu.jair@gmail.com'),
(5, 'pbkdf2_sha256$720000$FbrlPYcvqo681rvniWzfwb$J9IegzXwjyCaTqVxMnN7bDpo6fxJUyUFwng3y5nrRko=', '2024-04-10 00:22:45.981494', 0, 1, 1001272605, 'juan', 'camilo', 'rodriguez', 'martinez', '3214256785', 'juanito_alcachofa@gmail.com'),
(6, 'pbkdf2_sha256$720000$otKh9GzV54C5lH1yOgQgfY$KEoYaD0rIIGYCEfC59G6pe5CyKAZeosyhiLw0dR8o30=', '2024-06-30 03:14:27.661539', 0, 1, 1001282634, 'juanes', 'Juanes', 'rodriguez', 'pena', '3214183434', 'example@gmail.com'),
(7, '12345', '2024-07-01 01:37:03.000000', 0, 1, 324242354, 'sebastian', NULL, 'fernandez', NULL, '3242424', 'example2@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `administrador_usuario_admin_id_5503ac20_fk_user_app_usuario_id` (`usuario_admin_id`);

--
-- Indices de la tabla `admin_interface_theme`
--
ALTER TABLE `admin_interface_theme`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_interface_theme_name_30bda70f_uniq` (`name`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `calificacion_producto`
--
ALTER TABLE `calificacion_producto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_usuario_id_ff892797_fk_user_app_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_user_app_usuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empleados_usuario_id_6b032d2f_fk_user_app_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Factura_name_b7601f10_uniq` (`name`);

--
-- Indices de la tabla `factura_compra`
--
ALTER TABLE `factura_compra`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Factura de compra_empleados_id_fa45c2bb_fk_empleados_id` (`empleados_id`),
  ADD KEY `Factura de compra_proveedores_id_39b5a9b0_fk_proveedor_id` (`proveedores_id`);

--
-- Indices de la tabla `factura_producto`
--
ALTER TABLE `factura_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Factura Producto_calificacion_product_4326ea6a_fk_Calificac` (`calificacion_producto_id`),
  ADD KEY `Factura Producto_factura_id_4466b787_fk_Factura_id` (`factura_id`),
  ADD KEY `Factura Producto_producto_id_e1025cbf_fk_producto_id` (`producto_id`);

--
-- Indices de la tabla `factura_venta`
--
ALTER TABLE `factura_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Factura venta_cliente_id_27b237ef_fk_cliente_id` (`cliente_id`),
  ADD KEY `Factura venta_empleados_id_549945a6_fk_empleados_id` (`empleados_id`);

--
-- Indices de la tabla `materia_prima`
--
ALTER TABLE `materia_prima`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `orden_produccion`
--
ALTER TABLE `orden_produccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orden_produccion_materia_prima_id_f46999de_fk_Materia prima_id` (`materia_prima_id`),
  ADD KEY `orden_produccion_producto_id_445bae4d_fk_producto_id` (`producto_id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles_usuarios`
--
ALTER TABLE `roles_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roles_usuarios_rol_id_b0081cd4_fk_roles_id` (`rol_id`),
  ADD KEY `roles_usuarios_usuario_id_41607388_fk_user_app_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `shopping_cart_carrito`
--
ALTER TABLE `shopping_cart_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shopping_cart_carrito_usuario_id_7df501ed_fk_user_app_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `shopping_cart_itemcarrito`
--
ALTER TABLE `shopping_cart_itemcarrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shopping_cart_itemca_carrito_id_94b35e73_fk_shopping_` (`carrito_id`),
  ADD KEY `shopping_cart_itemcarrito_producto_id_409d76f6_fk_producto_id` (`producto_id`);

--
-- Indices de la tabla `shopping_cart_pedido`
--
ALTER TABLE `shopping_cart_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shopping_cart_pedido_usuario_id_ff14884f_fk_user_app_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `shopping_cart_pedido_items`
--
ALTER TABLE `shopping_cart_pedido_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `shopping_cart_pedido_ite_pedido_id_itemcarrito_id_5e111b35_uniq` (`pedido_id`,`itemcarrito_id`),
  ADD KEY `shopping_cart_pedido_itemcarrito_id_398980bb_fk_shopping_` (`itemcarrito_id`);

--
-- Indices de la tabla `user_app_usuario`
--
ALTER TABLE `user_app_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `admin_interface_theme`
--
ALTER TABLE `admin_interface_theme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT de la tabla `calificacion_producto`
--
ALTER TABLE `calificacion_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `factura_compra`
--
ALTER TABLE `factura_compra`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `factura_producto`
--
ALTER TABLE `factura_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `factura_venta`
--
ALTER TABLE `factura_venta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `materia_prima`
--
ALTER TABLE `materia_prima`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `orden_produccion`
--
ALTER TABLE `orden_produccion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `roles_usuarios`
--
ALTER TABLE `roles_usuarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `shopping_cart_carrito`
--
ALTER TABLE `shopping_cart_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `shopping_cart_itemcarrito`
--
ALTER TABLE `shopping_cart_itemcarrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `shopping_cart_pedido`
--
ALTER TABLE `shopping_cart_pedido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `shopping_cart_pedido_items`
--
ALTER TABLE `shopping_cart_pedido_items`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_app_usuario`
--
ALTER TABLE `user_app_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `administrador_usuario_admin_id_5503ac20_fk_user_app_usuario_id` FOREIGN KEY (`usuario_admin_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_usuario_id_ff892797_fk_user_app_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_app_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_usuario_id_6b032d2f_fk_user_app_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `factura_compra`
--
ALTER TABLE `factura_compra`
  ADD CONSTRAINT `Factura de compra_empleados_id_fa45c2bb_fk_empleados_id` FOREIGN KEY (`empleados_id`) REFERENCES `empleados` (`id`),
  ADD CONSTRAINT `Factura de compra_proveedores_id_39b5a9b0_fk_proveedor_id` FOREIGN KEY (`proveedores_id`) REFERENCES `proveedor` (`id`);

--
-- Filtros para la tabla `factura_producto`
--
ALTER TABLE `factura_producto`
  ADD CONSTRAINT `Factura Producto_calificacion_product_4326ea6a_fk_Calificac` FOREIGN KEY (`calificacion_producto_id`) REFERENCES `calificacion_producto` (`id`),
  ADD CONSTRAINT `Factura Producto_factura_id_4466b787_fk_Factura_id` FOREIGN KEY (`factura_id`) REFERENCES `factura` (`id`),
  ADD CONSTRAINT `Factura Producto_producto_id_e1025cbf_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `factura_venta`
--
ALTER TABLE `factura_venta`
  ADD CONSTRAINT `Factura venta_cliente_id_27b237ef_fk_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  ADD CONSTRAINT `Factura venta_empleados_id_549945a6_fk_empleados_id` FOREIGN KEY (`empleados_id`) REFERENCES `empleados` (`id`);

--
-- Filtros para la tabla `orden_produccion`
--
ALTER TABLE `orden_produccion`
  ADD CONSTRAINT `orden_produccion_materia_prima_id_f46999de_fk_Materia prima_id` FOREIGN KEY (`materia_prima_id`) REFERENCES `materia_prima` (`id`),
  ADD CONSTRAINT `orden_produccion_producto_id_445bae4d_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `roles_usuarios`
--
ALTER TABLE `roles_usuarios`
  ADD CONSTRAINT `roles_usuarios_rol_id_b0081cd4_fk_roles_id` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `roles_usuarios_usuario_id_41607388_fk_user_app_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `shopping_cart_carrito`
--
ALTER TABLE `shopping_cart_carrito`
  ADD CONSTRAINT `shopping_cart_carrito_usuario_id_7df501ed_fk_user_app_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `shopping_cart_itemcarrito`
--
ALTER TABLE `shopping_cart_itemcarrito`
  ADD CONSTRAINT `shopping_cart_itemca_carrito_id_94b35e73_fk_shopping_` FOREIGN KEY (`carrito_id`) REFERENCES `shopping_cart_carrito` (`id`),
  ADD CONSTRAINT `shopping_cart_itemcarrito_producto_id_409d76f6_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `shopping_cart_pedido`
--
ALTER TABLE `shopping_cart_pedido`
  ADD CONSTRAINT `shopping_cart_pedido_usuario_id_ff14884f_fk_user_app_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_app_usuario` (`id`);

--
-- Filtros para la tabla `shopping_cart_pedido_items`
--
ALTER TABLE `shopping_cart_pedido_items`
  ADD CONSTRAINT `shopping_cart_pedido_itemcarrito_id_398980bb_fk_shopping_` FOREIGN KEY (`itemcarrito_id`) REFERENCES `shopping_cart_itemcarrito` (`id`),
  ADD CONSTRAINT `shopping_cart_pedido_pedido_id_24f6a933_fk_shopping_` FOREIGN KEY (`pedido_id`) REFERENCES `shopping_cart_pedido` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
