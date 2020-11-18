/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : employees

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 18/11/2020 14:26:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` varchar(10) DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `english` double(3,1) DEFAULT NULL,
  `math` double(3,1) DEFAULT NULL,
  `chinese` double(3,1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'neo', '0', 99.0, 90.0, 99.5);
INSERT INTO `user` VALUES (2, 'tom', '1', 90.0, 86.5, 96.0);
INSERT INTO `user` VALUES (3, 'frank', '0', 99.0, 90.0, 99.5);
INSERT INTO `user` VALUES (4, 'lina', '1', 80.0, 86.5, 86.0);
INSERT INTO `user` VALUES (5, 'ming', '0', 99.0, 90.0, 99.5);
INSERT INTO `user` VALUES (6, 'sala', '0', 90.0, 86.5, 96.0);
INSERT INTO `user` VALUES (7, 'huhu', '1', 99.0, 90.0, 99.5);
INSERT INTO `user` VALUES (8, 'hah', '0', 80.0, 86.5, 86.0);
INSERT INTO `user` VALUES (9, 'lan', '1', 99.0, 90.0, 99.5);
INSERT INTO `user` VALUES (10, 'fang', '0', 80.0, 86.5, 86.0);
INSERT INTO `user` VALUES (12, 'leo', '0', 99.0, 90.0, 86.0);
INSERT INTO `user` VALUES (13, 'leo', '0', 99.0, 90.0, 86.0);
INSERT INTO `user` VALUES (14, 'leo', '0', 99.0, 90.0, 86.0);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
