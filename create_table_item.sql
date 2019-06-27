CREATE TABLE item (
    item_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    brands VARCHAR(255),
    wsp INT NOT NULL,
    stores VARCHAR(1024),
    PRIMARY KEY(item_id)
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;

ALTER TABLE item 
    ADD CONSTRAINT fk_item_to_store
    FOREIGN KEY () REFERENCES stores(item_id);

CREATE TABLE stores (
    item_id INT NOT NULL,
    store_id INT NOT NULL UNIQUE,
    store_name VARCHAR(255) NOT NULL UNIQUE,
    distance INT NOT NULL,
    markup FLOAT(5, 2) NOT NULL,
    PRIMARY KEY(store_id)
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;
