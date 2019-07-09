CREATE TABLE `file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(200) DEFAULT NULL,
  `folder` varchar(200) default null,
  `name` varchar(100) DEFAULT NULL,
  `extension` varchar(20) DEFAULT NULL,
  `size` bigint DEFAULT NULL,
  `created_at` char(14) DEFAULT NULL,
  `modified_at` char(14) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;