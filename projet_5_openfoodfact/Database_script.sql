CREATE TABLE IF NOT EXISTS `Category`(
  `id`   INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
PRIMARY KEY(`id`))
ENGINE = InnoDB DEFAULT CHARACTER
SET = utf8
;

CREATE TABLE IF NOT EXISTS `Product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `barcode`BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(220) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  `link` VARCHAR(60) NOT NULL,
  `nutriscore` VARCHAR(1) NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`), INDEX `fk_cate_idx`(`category_id` ASC)VISIBLE,
CONSTRAINT `fk_cate`
FOREIGN KEY(`category_id`)
REFERENCES `Category`(`id`)
  ON
DELETE NO ACTION ON
UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS substitute (
  product_id INT NOT NULL,
  productsub_id INT NOT NULL,
  PRIMARY KEY (product_id, productsub_id),
FOREIGN KEY(product_id)
REFERENCES Product(id),
FOREIGN KEY(productsub_id)
REFERENCES Product(id))
ENGINE = InnoDB;

