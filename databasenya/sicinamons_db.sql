-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 10, 2025 at 12:27 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sicinamons_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `datasensor`
--

CREATE TABLE `datasensor` (
  `id_data` int NOT NULL,
  `id_larik` int NOT NULL,
  `nomor_pohon` int DEFAULT NULL,
  `waktu_data` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `nitrogen` decimal(10,2) DEFAULT NULL,
  `fosfor` decimal(10,2) DEFAULT NULL,
  `kalium` decimal(10,2) DEFAULT NULL,
  `ph` decimal(4,2) DEFAULT NULL,
  `suhu` decimal(5,2) DEFAULT NULL,
  `kelembaban` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Menyimpan data historis nutrisi dan lingkungan dari sensor';

-- --------------------------------------------------------

--
-- Table structure for table `larik`
--

CREATE TABLE `larik` (
  `id_larik` int NOT NULL,
  `id_pengguna` int NOT NULL,
  `nama_larik` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `info_lokasi` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Merepresentasikan area atau larik tanaman yang dipantau';

--
-- Dumping data for table `larik`
--

INSERT INTO `larik` (`id_larik`, `id_pengguna`, `nama_larik`, `info_lokasi`) VALUES
(1, 2, 'Larik A', 'Banjar'),
(2, 3, 'Larik B', 'Banjar');

-- --------------------------------------------------------

--
-- Table structure for table `logpenyiraman`
--

CREATE TABLE `logpenyiraman` (
  `id_log` int NOT NULL,
  `id_larik` int NOT NULL,
  `id_pengguna` int DEFAULT NULL,
  `waktu_aksi` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `jumlah_nitrogen` decimal(10,2) DEFAULT '0.00',
  `jumlah_fosfor` decimal(10,2) DEFAULT '0.00',
  `jumlah_kalium` decimal(10,2) DEFAULT '0.00',
  `jumlah_air` decimal(10,2) DEFAULT '0.00',
  `durasi_detik` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Mencatat riwayat aksi pemupukan dan penyiraman';

-- --------------------------------------------------------

--
-- Table structure for table `logperkembangan`
--

CREATE TABLE `logperkembangan` (
  `id_log` int NOT NULL,
  `id_pengguna` int DEFAULT NULL,
  `nomor_pohon` int NOT NULL,
  `waktu_catat` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `diameter` decimal(10,2) NOT NULL,
  `tinggi` decimal(10,2) NOT NULL,
  `hitung_biomassa` decimal(10,2) DEFAULT NULL,
  `hitung_minyak_min` decimal(10,2) DEFAULT NULL,
  `hitung_minyak_max` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Menyimpan catatan manual pertumbuhan tanaman oleh petani';

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id_pengguna` int NOT NULL,
  `nama_pengguna` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `hash_kata_sandi` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Menyimpan data akun pengguna (petani)';

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id_pengguna`, `nama_pengguna`, `email`, `hash_kata_sandi`) VALUES
(2, 'Simanis', 'asu@gmail.com', 'dwa'),
(3, 'Riduan', 'wan@gmail.com', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `datasensor`
--
ALTER TABLE `datasensor`
  ADD PRIMARY KEY (`id_data`),
  ADD KEY `id_larik` (`id_larik`);

--
-- Indexes for table `larik`
--
ALTER TABLE `larik`
  ADD PRIMARY KEY (`id_larik`),
  ADD KEY `id_pengguna` (`id_pengguna`);

--
-- Indexes for table `logpenyiraman`
--
ALTER TABLE `logpenyiraman`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `id_larik` (`id_larik`),
  ADD KEY `id_pengguna` (`id_pengguna`);

--
-- Indexes for table `logperkembangan`
--
ALTER TABLE `logperkembangan`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `id_pengguna` (`id_pengguna`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id_pengguna`),
  ADD UNIQUE KEY `nama_pengguna` (`nama_pengguna`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `datasensor`
--
ALTER TABLE `datasensor`
  MODIFY `id_data` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `larik`
--
ALTER TABLE `larik`
  MODIFY `id_larik` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `logpenyiraman`
--
ALTER TABLE `logpenyiraman`
  MODIFY `id_log` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `logperkembangan`
--
ALTER TABLE `logperkembangan`
  MODIFY `id_log` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id_pengguna` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `datasensor`
--
ALTER TABLE `datasensor`
  ADD CONSTRAINT `datasensor_ibfk_1` FOREIGN KEY (`id_larik`) REFERENCES `larik` (`id_larik`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `larik`
--
ALTER TABLE `larik`
  ADD CONSTRAINT `larik_ibfk_1` FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id_pengguna`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `logpenyiraman`
--
ALTER TABLE `logpenyiraman`
  ADD CONSTRAINT `logpenyiraman_ibfk_1` FOREIGN KEY (`id_larik`) REFERENCES `larik` (`id_larik`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `logpenyiraman_ibfk_2` FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id_pengguna`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `logperkembangan`
--
ALTER TABLE `logperkembangan`
  ADD CONSTRAINT `logperkembangan_ibfk_1` FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id_pengguna`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
