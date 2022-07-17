CREATE TABLE `pet` (
  `name` varchar(20) NOT NULL,
  `owner` varchar(20) NOT NULL,
  `species` varchar(20) NOT NULL,
  `sex` char(1) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `pet`
  ADD PRIMARY KEY (`name`);