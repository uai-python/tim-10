-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2017 at 01:00 PM
-- Server version: 5.6.14
-- PHP Version: 5.5.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dataquiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `data pengguna`
--

CREATE TABLE IF NOT EXISTS `data pengguna` (
  `nama` varchar(50) NOT NULL,
  `jeniskelamin` varchar(15) NOT NULL,
  `kota` varchar(15) NOT NULL,
  `no` int(5) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `pertanyaan`
--

CREATE TABLE IF NOT EXISTS `pertanyaan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pertanyaan` longtext NOT NULL,
  `jawaban` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `pertanyaan`
--

INSERT INTO `pertanyaan` (`id`, `pertanyaan`, `jawaban`) VALUES
(1, 'Pada wilayah Provinsi DKI Jakarta, berapa banyak sekolah yang belum memiliki status akreditasi', '358'),
(2, 'Berapa jumlah presentase sekolah di Jakarta Barat yang memiliki status akreditasi A pada semua jenjang', '56,75%'),
(3, 'Berapa jumlah sekolah jenjang SMK yang memiliki status akreditasi A yang ada di wilayah Jakarta Pusat', '34'),
(4, 'Di kepuaulan seribu, ada berapa banyak sekolah yang memiliki status akreditasi B pada semua jenjang', '12'),
(5, 'berapa jumlah sekolah di Provinsi DKI Jakarta yang memiliki status akreditasi B dan C', '1568'),
(6, 'Di tahun 2014, berapa nilai rata-rata hasil Ujian Nasional pada semua jenjang sekolah', '34,9'),
(7, 'Berapa nilai tertinggi hasil Ujian Nasional tahun 2012 di jenjang SMA IPA ', '58.45'),
(8, 'Berapa nilai terendah hasil Ujian Nasional di tahun 2013 pada jenjang SMP', '8,65');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
