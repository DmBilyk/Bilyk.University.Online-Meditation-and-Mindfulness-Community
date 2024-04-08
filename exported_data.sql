BEGIN TRANSACTION;
CREATE TABLE "Forum_post"
(
    "id"         integer  NOT NULL PRIMARY KEY AUTOINCREMENT,
    "message"    text     NOT NULL,
    "created_at" datetime NOT NULL,
    "user_id"    integer  NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "Forum_post"
VALUES (18, '-The "User Profile" section does not display BIO after saving.-Fixed.', '2024-04-02 15:58:22.901829', 1);
INSERT INTO "Forum_post"
VALUES (19, '-No option to add a profile photo. Coming soon', '2024-04-02 15:58:29.482624', 1);
INSERT INTO "Forum_post"
VALUES (20, '-The site footer needs to correct "freeback" instead of "freeback".-Fixed.', '2024-04-02 15:58:38.341845',
        1);
INSERT INTO "Forum_post"
VALUES (21, '-Forum have no option to reply to a user and create your own wall on a question you interested in.',
        '2024-04-02 15:58:46.495925', 1);
INSERT INTO "Forum_post"
VALUES (22, '-No "back" button when leaving a page with meditation video from youtube. -Fixed.',
        '2024-04-02 15:58:56.363059', 1);
INSERT INTO "Forum_post"
VALUES (23,
        '-The section with tasks is useless if it is not logically connected to the parts of the site, which would be a task. -Fixed.',
        '2024-04-02 15:59:05.165738', 1);
INSERT INTO "Forum_post"
VALUES (24, '-Cute loading wheel. - Thank you for your feedback', '2024-04-02 15:59:11.401239', 1);
CREATE TABLE "Forum_response"
(
    "id"             integer  NOT NULL PRIMARY KEY AUTOINCREMENT,
    "message"        text     NOT NULL,
    "created_at"     datetime NOT NULL,
    "parent_post_id" bigint   NOT NULL REFERENCES "Forum_post" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "WEB_profile"
(
    "id"        integer          NOT NULL PRIMARY KEY AUTOINCREMENT,
    "age"       integer unsigned NULL CHECK ("age" >= 0),
    "country"   varchar(2)       NULL,
    "bio"       text             NOT NULL,
    "user_id"   integer          NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "level"     varchar(3)       NULL,
    "google_id" varchar(255)     NULL UNIQUE
);
INSERT INTO "WEB_profile"
VALUES (1, NULL, NULL, '', 4, NULL, NULL);
INSERT INTO "WEB_profile"
VALUES (2, NULL, NULL, '', 1, NULL, NULL);
INSERT INTO "WEB_profile"
VALUES (3, NULL, NULL, 'льдлівмвам', 5, NULL, NULL);
CREATE TABLE "WEB_task"
(
    "id"          integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "description" varchar(255) NOT NULL,
    "completed"   bool         NOT NULL,
    "user_id"     integer      NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "last_reset"  datetime     NOT NULL,
    "time"        time         NOT NULL,
    "category_id" bigint       NULL REFERENCES "WEB_taskcategory" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "WEB_taskcategory"
(
    "id"          integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name"        varchar(100) NOT NULL,
    "description" text         NOT NULL,
    "color"       varchar(7)   NOT NULL
);
INSERT INTO "WEB_taskcategory"
VALUES (1, 'Short Meditation', '', '#007bff');
CREATE TABLE "WEB_userprofile"
(
    "id"           integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "google_email" varchar(254) NOT NULL,
    "google_name"  varchar(255) NOT NULL,
    "user_id"      integer      NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "events"       text         NOT NULL
);
INSERT INTO "WEB_userprofile"
VALUES (3, '', '', 1, ',F,Hi my name is');
INSERT INTO "WEB_userprofile"
VALUES (4, '', '', 4, '');
INSERT INTO "WEB_userprofile"
VALUES (5, '', '', 5, '');
CREATE TABLE "WEB_video"
(
    "id"           integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title"        varchar(100) NOT NULL,
    "description"  text         NOT NULL,
    "youtube_link" varchar(200) NOT NULL,
    "image_url"    varchar(200) NOT NULL
);
INSERT INTO "WEB_video"
VALUES (3, 'Meditadion', 'Meditan', 'https://www.youtube.com/watch?v=inpok4MKVLM',
        'https://images.everydayhealth.com/images/emotional-health/meditation/a-complete-guide-to-meditation-722x406.jpg?sfvrsn=e47f03cd_1');
CREATE TABLE "account_emailaddress"
(
    "id"       integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "verified" bool         NOT NULL,
    "primary"  bool         NOT NULL,
    "user_id"  integer      NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "email"    varchar(254) NOT NULL
);
INSERT INTO "account_emailaddress"
VALUES (3, 1, 1, 4, 'dima.bilik2005@gmail.com');
INSERT INTO "account_emailaddress"
VALUES (4, 1, 1, 5, 'exe24876@gmail.com');
CREATE TABLE "account_emailconfirmation"
(
    "id"               integer     NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created"          datetime    NOT NULL,
    "sent"             datetime    NULL,
    "key"              varchar(64) NOT NULL UNIQUE,
    "email_address_id" integer     NOT NULL REFERENCES "account_emailaddress" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "auth_group"
(
    "id"   integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(150) NOT NULL UNIQUE
);
CREATE TABLE "auth_group_permissions"
(
    "id"            integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "group_id"      integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "auth_permission"
(
    "id"              integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "content_type_id" integer      NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "codename"        varchar(100) NOT NULL,
    "name"            varchar(255) NOT NULL
);
INSERT INTO "auth_permission"
VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO "auth_permission"
VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO "auth_permission"
VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO "auth_permission"
VALUES (4, 1, 'view_logentry', 'Can view log entry');
INSERT INTO "auth_permission"
VALUES (5, 2, 'add_permission', 'Can add permission');
INSERT INTO "auth_permission"
VALUES (6, 2, 'change_permission', 'Can change permission');
INSERT INTO "auth_permission"
VALUES (7, 2, 'delete_permission', 'Can delete permission');
INSERT INTO "auth_permission"
VALUES (8, 2, 'view_permission', 'Can view permission');
INSERT INTO "auth_permission"
VALUES (9, 3, 'add_group', 'Can add group');
INSERT INTO "auth_permission"
VALUES (10, 3, 'change_group', 'Can change group');
INSERT INTO "auth_permission"
VALUES (11, 3, 'delete_group', 'Can delete group');
INSERT INTO "auth_permission"
VALUES (12, 3, 'view_group', 'Can view group');
INSERT INTO "auth_permission"
VALUES (13, 4, 'add_user', 'Can add user');
INSERT INTO "auth_permission"
VALUES (14, 4, 'change_user', 'Can change user');
INSERT INTO "auth_permission"
VALUES (15, 4, 'delete_user', 'Can delete user');
INSERT INTO "auth_permission"
VALUES (16, 4, 'view_user', 'Can view user');
INSERT INTO "auth_permission"
VALUES (17, 5, 'add_contenttype', 'Can add content type');
INSERT INTO "auth_permission"
VALUES (18, 5, 'change_contenttype', 'Can change content type');
INSERT INTO "auth_permission"
VALUES (19, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO "auth_permission"
VALUES (20, 5, 'view_contenttype', 'Can view content type');
INSERT INTO "auth_permission"
VALUES (21, 6, 'add_session', 'Can add session');
INSERT INTO "auth_permission"
VALUES (22, 6, 'change_session', 'Can change session');
INSERT INTO "auth_permission"
VALUES (23, 6, 'delete_session', 'Can delete session');
INSERT INTO "auth_permission"
VALUES (24, 6, 'view_session', 'Can view session');
INSERT INTO "auth_permission"
VALUES (25, 7, 'add_site', 'Can add site');
INSERT INTO "auth_permission"
VALUES (26, 7, 'change_site', 'Can change site');
INSERT INTO "auth_permission"
VALUES (27, 7, 'delete_site', 'Can delete site');
INSERT INTO "auth_permission"
VALUES (28, 7, 'view_site', 'Can view site');
INSERT INTO "auth_permission"
VALUES (29, 8, 'add_emailaddress', 'Can add email address');
INSERT INTO "auth_permission"
VALUES (30, 8, 'change_emailaddress', 'Can change email address');
INSERT INTO "auth_permission"
VALUES (31, 8, 'delete_emailaddress', 'Can delete email address');
INSERT INTO "auth_permission"
VALUES (32, 8, 'view_emailaddress', 'Can view email address');
INSERT INTO "auth_permission"
VALUES (33, 9, 'add_emailconfirmation', 'Can add email confirmation');
INSERT INTO "auth_permission"
VALUES (34, 9, 'change_emailconfirmation', 'Can change email confirmation');
INSERT INTO "auth_permission"
VALUES (35, 9, 'delete_emailconfirmation', 'Can delete email confirmation');
INSERT INTO "auth_permission"
VALUES (36, 9, 'view_emailconfirmation', 'Can view email confirmation');
INSERT INTO "auth_permission"
VALUES (37, 10, 'add_socialaccount', 'Can add social account');
INSERT INTO "auth_permission"
VALUES (38, 10, 'change_socialaccount', 'Can change social account');
INSERT INTO "auth_permission"
VALUES (39, 10, 'delete_socialaccount', 'Can delete social account');
INSERT INTO "auth_permission"
VALUES (40, 10, 'view_socialaccount', 'Can view social account');
INSERT INTO "auth_permission"
VALUES (41, 11, 'add_socialapp', 'Can add social application');
INSERT INTO "auth_permission"
VALUES (42, 11, 'change_socialapp', 'Can change social application');
INSERT INTO "auth_permission"
VALUES (43, 11, 'delete_socialapp', 'Can delete social application');
INSERT INTO "auth_permission"
VALUES (44, 11, 'view_socialapp', 'Can view social application');
INSERT INTO "auth_permission"
VALUES (45, 12, 'add_socialtoken', 'Can add social application token');
INSERT INTO "auth_permission"
VALUES (46, 12, 'change_socialtoken', 'Can change social application token');
INSERT INTO "auth_permission"
VALUES (47, 12, 'delete_socialtoken', 'Can delete social application token');
INSERT INTO "auth_permission"
VALUES (48, 12, 'view_socialtoken', 'Can view social application token');
INSERT INTO "auth_permission"
VALUES (49, 13, 'add_userprofile', 'Can add user profile');
INSERT INTO "auth_permission"
VALUES (50, 13, 'change_userprofile', 'Can change user profile');
INSERT INTO "auth_permission"
VALUES (51, 13, 'delete_userprofile', 'Can delete user profile');
INSERT INTO "auth_permission"
VALUES (52, 13, 'view_userprofile', 'Can view user profile');
INSERT INTO "auth_permission"
VALUES (53, 14, 'add_profile', 'Can add profile');
INSERT INTO "auth_permission"
VALUES (54, 14, 'change_profile', 'Can change profile');
INSERT INTO "auth_permission"
VALUES (55, 14, 'delete_profile', 'Can delete profile');
INSERT INTO "auth_permission"
VALUES (56, 14, 'view_profile', 'Can view profile');
INSERT INTO "auth_permission"
VALUES (57, 15, 'add_video', 'Can add video');
INSERT INTO "auth_permission"
VALUES (58, 15, 'change_video', 'Can change video');
INSERT INTO "auth_permission"
VALUES (59, 15, 'delete_video', 'Can delete video');
INSERT INTO "auth_permission"
VALUES (60, 15, 'view_video', 'Can view video');
INSERT INTO "auth_permission"
VALUES (61, 16, 'add_feedback', 'Can add feedback');
INSERT INTO "auth_permission"
VALUES (62, 16, 'change_feedback', 'Can change feedback');
INSERT INTO "auth_permission"
VALUES (63, 16, 'delete_feedback', 'Can delete feedback');
INSERT INTO "auth_permission"
VALUES (64, 16, 'view_feedback', 'Can view feedback');
INSERT INTO "auth_permission"
VALUES (65, 17, 'add_product', 'Can add product');
INSERT INTO "auth_permission"
VALUES (66, 17, 'change_product', 'Can change product');
INSERT INTO "auth_permission"
VALUES (67, 17, 'delete_product', 'Can delete product');
INSERT INTO "auth_permission"
VALUES (68, 17, 'view_product', 'Can view product');
INSERT INTO "auth_permission"
VALUES (69, 18, 'add_product', 'Can add product');
INSERT INTO "auth_permission"
VALUES (70, 18, 'change_product', 'Can change product');
INSERT INTO "auth_permission"
VALUES (71, 18, 'delete_product', 'Can delete product');
INSERT INTO "auth_permission"
VALUES (72, 18, 'view_product', 'Can view product');
INSERT INTO "auth_permission"
VALUES (73, 19, 'add_feedback', 'Can add feedback');
INSERT INTO "auth_permission"
VALUES (74, 19, 'change_feedback', 'Can change feedback');
INSERT INTO "auth_permission"
VALUES (75, 19, 'delete_feedback', 'Can delete feedback');
INSERT INTO "auth_permission"
VALUES (76, 19, 'view_feedback', 'Can view feedback');
INSERT INTO "auth_permission"
VALUES (77, 20, 'add_post', 'Can add post');
INSERT INTO "auth_permission"
VALUES (78, 20, 'change_post', 'Can change post');
INSERT INTO "auth_permission"
VALUES (79, 20, 'delete_post', 'Can delete post');
INSERT INTO "auth_permission"
VALUES (80, 20, 'view_post', 'Can view post');
INSERT INTO "auth_permission"
VALUES (81, 21, 'add_personalcalendar', 'Can add personal calendar');
INSERT INTO "auth_permission"
VALUES (82, 21, 'change_personalcalendar', 'Can change personal calendar');
INSERT INTO "auth_permission"
VALUES (83, 21, 'delete_personalcalendar', 'Can delete personal calendar');
INSERT INTO "auth_permission"
VALUES (84, 21, 'view_personalcalendar', 'Can view personal calendar');
INSERT INTO "auth_permission"
VALUES (85, 22, 'add_task', 'Can add task');
INSERT INTO "auth_permission"
VALUES (86, 22, 'change_task', 'Can change task');
INSERT INTO "auth_permission"
VALUES (87, 22, 'delete_task', 'Can delete task');
INSERT INTO "auth_permission"
VALUES (88, 22, 'view_task', 'Can view task');
INSERT INTO "auth_permission"
VALUES (89, 23, 'add_response', 'Can add response');
INSERT INTO "auth_permission"
VALUES (90, 23, 'change_response', 'Can change response');
INSERT INTO "auth_permission"
VALUES (91, 23, 'delete_response', 'Can delete response');
INSERT INTO "auth_permission"
VALUES (92, 23, 'view_response', 'Can view response');
INSERT INTO "auth_permission"
VALUES (93, 24, 'add_taskcategory', 'Can add task category');
INSERT INTO "auth_permission"
VALUES (94, 24, 'change_taskcategory', 'Can change task category');
INSERT INTO "auth_permission"
VALUES (95, 24, 'delete_taskcategory', 'Can delete task category');
INSERT INTO "auth_permission"
VALUES (96, 24, 'view_taskcategory', 'Can view task category');
CREATE TABLE "auth_user"
(
    "id"           integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password"     varchar(128) NOT NULL,
    "last_login"   datetime     NULL,
    "is_superuser" bool         NOT NULL,
    "username"     varchar(150) NOT NULL UNIQUE,
    "last_name"    varchar(150) NOT NULL,
    "email"        varchar(254) NOT NULL,
    "is_staff"     bool         NOT NULL,
    "is_active"    bool         NOT NULL,
    "date_joined"  datetime     NOT NULL,
    "first_name"   varchar(150) NOT NULL
);
INSERT INTO "auth_user"
VALUES (1, 'pbkdf2_sha256$720000$3ZJqiwq37xuYgbRkXLVJY4$tg2ItaedzKsEC2dm0Rnv+GQ6yWBL4qpYCL2uQQ+ANZc=',
        '2024-04-02 15:57:45.703006', 1, 'mackbook', '', 'dmbilyk3861@gmail.com', 1, 1, '2024-03-04 17:09:15.806016',
        '');
INSERT INTO "auth_user"
VALUES (4, '!8fsekpKrw4734oLqbscqFYIDxRqQgnWLBT0amCSz', '2024-03-27 17:49:21.910712', 0, 'dima', 'Bilik',
        'dima.bilik2005@gmail.com', 0, 1, '2024-03-20 14:31:53.402273', 'DIma');
INSERT INTO "auth_user"
VALUES (5, '!fU3cScyf92D4r1hTzRDaxDw7PE6uwgct7ZKYmlCW', '2024-04-02 13:57:50.974950', 0, 'dmytro', '',
        'exe24876@gmail.com', 0, 1, '2024-04-02 13:57:50.939761', 'Dmytro');
CREATE TABLE "auth_user_groups"
(
    "id"       integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id"  integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "auth_user_user_permissions"
(
    "id"            integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id"       integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "django_admin_log"
(
    "id"              integer           NOT NULL PRIMARY KEY AUTOINCREMENT,
    "object_id"       text              NULL,
    "object_repr"     varchar(200)      NOT NULL,
    "action_flag"     smallint unsigned NOT NULL CHECK ("action_flag" >= 0),
    "change_message"  text              NOT NULL,
    "content_type_id" integer           NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id"         integer           NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "action_time"     datetime          NOT NULL
);
INSERT INTO "django_admin_log"
VALUES (1, '1', 'http://127.0.0.1:8000/', 2, '[{"changed": {"fields": ["Domain name", "Display name"]}}]', 7, 1,
        '2024-03-04 17:10:01.101528');
INSERT INTO "django_admin_log"
VALUES (2, '1', 'Google Authorization', 1, '[{"added": {}}]', 11, 1, '2024-03-04 17:29:23.869189');
INSERT INTO "django_admin_log"
VALUES (3, '1', 'calm-connections.azurewebsites.net', 2, '[{"changed": {"fields": ["Domain name", "Display name"]}}]',
        7, 1, '2024-03-09 09:39:44.936666');
INSERT INTO "django_admin_log"
VALUES (4, '1', 'Google Authorization', 2, '[]', 11, 1, '2024-03-09 09:40:00.240192');
INSERT INTO "django_admin_log"
VALUES (5, '2', 'http://127.0.0.1:8000/', 1, '[{"added": {}}]', 7, 1, '2024-03-20 14:21:01.031472');
INSERT INTO "django_admin_log"
VALUES (6, '1', 'Google Authorization', 2, '[{"changed": {"fields": ["Sites"]}}]', 11, 1, '2024-03-20 14:21:12.442033');
INSERT INTO "django_admin_log"
VALUES (7, '3', 'dmytro', 3, '', 4, 1, '2024-03-20 14:22:54.058050');
INSERT INTO "django_admin_log"
VALUES (8, '2', 'nick', 3, '', 4, 1, '2024-03-20 14:22:54.062381');
INSERT INTO "django_admin_log"
VALUES (9, '1', 'My video', 1, '[{"added": {}}]', 15, 1, '2024-03-20 14:27:43.594674');
INSERT INTO "django_admin_log"
VALUES (10, '1', 'Google Authorization', 2, '[{"changed": {"fields": ["Client id", "Secret key"]}}]', 11, 1,
        '2024-03-20 14:31:13.282404');
INSERT INTO "django_admin_log"
VALUES (11, '1', 'My video', 2, '[{"changed": {"fields": ["Image", "File"]}}]', 15, 1, '2024-03-22 06:40:02.194925');
INSERT INTO "django_admin_log"
VALUES (12, '1', 'Authorization', 1, '[{"added": {}}]', 17, 1, '2024-03-25 15:21:42.654814');
INSERT INTO "django_admin_log"
VALUES (13, '1', 'Authorization', 2, '[]', 17, 1, '2024-03-25 15:21:45.952094');
INSERT INTO "django_admin_log"
VALUES (14, '2', 'Customization', 1, '[{"added": {}}]', 17, 1, '2024-03-25 15:22:21.308221');
INSERT INTO "django_admin_log"
VALUES (15, '3', 'Guided Meditation', 1, '[{"added": {}}]', 17, 1, '2024-03-25 15:22:33.235381');
INSERT INTO "django_admin_log"
VALUES (16, '1', 'Customization', 1, '[{"added": {}}]', 18, 1, '2024-03-25 15:29:17.082544');
INSERT INTO "django_admin_log"
VALUES (17, '2', 'Hello world', 1, '[{"added": {}}]', 15, 1, '2024-03-30 15:32:05.906277');
INSERT INTO "django_admin_log"
VALUES (18, '2', 'Hello world', 2, '[{"changed": {"fields": ["Image"]}}]', 15, 1, '2024-03-30 15:45:59.161529');
INSERT INTO "django_admin_log"
VALUES (19, '2', 'Hello world', 3, '', 15, 1, '2024-03-30 15:53:44.309253');
INSERT INTO "django_admin_log"
VALUES (20, '1', 'My video', 3, '', 15, 1, '2024-03-30 15:53:44.313655');
INSERT INTO "django_admin_log"
VALUES (21, '3', 'Meditadion', 1, '[{"added": {}}]', 15, 1, '2024-03-30 15:54:22.550618');
INSERT INTO "django_admin_log"
VALUES (22, '17', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.427241');
INSERT INTO "django_admin_log"
VALUES (23, '16', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.433529');
INSERT INTO "django_admin_log"
VALUES (24, '15', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.435529');
INSERT INTO "django_admin_log"
VALUES (25, '14', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.437057');
INSERT INTO "django_admin_log"
VALUES (26, '13', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.439195');
INSERT INTO "django_admin_log"
VALUES (27, '12', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.440666');
INSERT INTO "django_admin_log"
VALUES (28, '11', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.441948');
INSERT INTO "django_admin_log"
VALUES (29, '10', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.443139');
INSERT INTO "django_admin_log"
VALUES (30, '9', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.444389');
INSERT INTO "django_admin_log"
VALUES (31, '8', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.445956');
INSERT INTO "django_admin_log"
VALUES (32, '7', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.447118');
INSERT INTO "django_admin_log"
VALUES (33, '6', 'Post by dmytro', 3, '', 20, 1, '2024-04-02 15:58:02.448207');
INSERT INTO "django_admin_log"
VALUES (34, '5', 'Post by dima', 3, '', 20, 1, '2024-04-02 15:58:02.449213');
INSERT INTO "django_admin_log"
VALUES (35, '4', 'Post by dima', 3, '', 20, 1, '2024-04-02 15:58:02.450048');
INSERT INTO "django_admin_log"
VALUES (36, '3', 'Post by dima', 3, '', 20, 1, '2024-04-02 15:58:02.450877');
INSERT INTO "django_admin_log"
VALUES (37, '2', 'Post by dima', 3, '', 20, 1, '2024-04-02 15:58:02.451773');
INSERT INTO "django_admin_log"
VALUES (38, '1', 'Post by dima', 3, '', 20, 1, '2024-04-02 15:58:02.452643');
INSERT INTO "django_admin_log"
VALUES (39, '1', 'Short Meditation', 1, '[{"added": {}}]', 24, 1, '2024-04-02 16:05:22.465393');
CREATE TABLE "django_content_type"
(
    "id"        integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" varchar(100) NOT NULL,
    "model"     varchar(100) NOT NULL
);
INSERT INTO "django_content_type"
VALUES (1, 'admin', 'logentry');
INSERT INTO "django_content_type"
VALUES (2, 'auth', 'permission');
INSERT INTO "django_content_type"
VALUES (3, 'auth', 'group');
INSERT INTO "django_content_type"
VALUES (4, 'auth', 'user');
INSERT INTO "django_content_type"
VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO "django_content_type"
VALUES (6, 'sessions', 'session');
INSERT INTO "django_content_type"
VALUES (7, 'sites', 'site');
INSERT INTO "django_content_type"
VALUES (8, 'account', 'emailaddress');
INSERT INTO "django_content_type"
VALUES (9, 'account', 'emailconfirmation');
INSERT INTO "django_content_type"
VALUES (10, 'socialaccount', 'socialaccount');
INSERT INTO "django_content_type"
VALUES (11, 'socialaccount', 'socialapp');
INSERT INTO "django_content_type"
VALUES (12, 'socialaccount', 'socialtoken');
INSERT INTO "django_content_type"
VALUES (13, 'WEB', 'userprofile');
INSERT INTO "django_content_type"
VALUES (14, 'WEB', 'profile');
INSERT INTO "django_content_type"
VALUES (15, 'WEB', 'video');
INSERT INTO "django_content_type"
VALUES (16, 'form', 'feedback');
INSERT INTO "django_content_type"
VALUES (17, 'form', 'product');
INSERT INTO "django_content_type"
VALUES (18, 'feedback', 'product');
INSERT INTO "django_content_type"
VALUES (19, 'feedback', 'feedback');
INSERT INTO "django_content_type"
VALUES (20, 'Forum', 'post');
INSERT INTO "django_content_type"
VALUES (21, 'WEB', 'personalcalendar');
INSERT INTO "django_content_type"
VALUES (22, 'WEB', 'task');
INSERT INTO "django_content_type"
VALUES (23, 'Forum', 'response');
INSERT INTO "django_content_type"
VALUES (24, 'WEB', 'taskcategory');
CREATE TABLE "django_migrations"
(
    "id"      integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app"     varchar(255) NOT NULL,
    "name"    varchar(255) NOT NULL,
    "applied" datetime     NOT NULL
);
INSERT INTO "django_migrations"
VALUES (1, 'contenttypes', '0001_initial', '2024-03-04 16:38:30.976329');
INSERT INTO "django_migrations"
VALUES (2, 'auth', '0001_initial', '2024-03-04 16:38:30.988022');
INSERT INTO "django_migrations"
VALUES (3, 'admin', '0001_initial', '2024-03-04 16:38:30.991217');
INSERT INTO "django_migrations"
VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-03-04 16:38:30.994813');
INSERT INTO "django_migrations"
VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-04 16:38:30.997003');
INSERT INTO "django_migrations"
VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2024-03-04 16:38:31.002583');
INSERT INTO "django_migrations"
VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2024-03-04 16:38:31.006798');
INSERT INTO "django_migrations"
VALUES (8, 'auth', '0003_alter_user_email_max_length', '2024-03-04 16:38:31.010352');
INSERT INTO "django_migrations"
VALUES (9, 'auth', '0004_alter_user_username_opts', '2024-03-04 16:38:31.012552');
INSERT INTO "django_migrations"
VALUES (10, 'auth', '0005_alter_user_last_login_null', '2024-03-04 16:38:31.015665');
INSERT INTO "django_migrations"
VALUES (11, 'auth', '0006_require_contenttypes_0002', '2024-03-04 16:38:31.016061');
INSERT INTO "django_migrations"
VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2024-03-04 16:38:31.018305');
INSERT INTO "django_migrations"
VALUES (13, 'auth', '0008_alter_user_username_max_length', '2024-03-04 16:38:31.021672');
INSERT INTO "django_migrations"
VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2024-03-04 16:38:31.024673');
INSERT INTO "django_migrations"
VALUES (15, 'auth', '0010_alter_group_name_max_length', '2024-03-04 16:38:31.027713');
INSERT INTO "django_migrations"
VALUES (16, 'auth', '0011_update_proxy_permissions', '2024-03-04 16:38:31.029857');
INSERT INTO "django_migrations"
VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2024-03-04 16:38:31.034619');
INSERT INTO "django_migrations"
VALUES (18, 'sessions', '0001_initial', '2024-03-04 16:38:31.036036');
INSERT INTO "django_migrations"
VALUES (19, 'account', '0001_initial', '2024-03-04 17:06:15.368851');
INSERT INTO "django_migrations"
VALUES (20, 'account', '0002_email_max_length', '2024-03-04 17:06:15.372510');
INSERT INTO "django_migrations"
VALUES (21, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2024-03-04 17:06:15.377447');
INSERT INTO "django_migrations"
VALUES (22, 'account', '0004_alter_emailaddress_drop_unique_email', '2024-03-04 17:06:15.381049');
INSERT INTO "django_migrations"
VALUES (23, 'account', '0005_emailaddress_idx_upper_email', '2024-03-04 17:06:15.383660');
INSERT INTO "django_migrations"
VALUES (24, 'sites', '0001_initial', '2024-03-04 17:06:15.384568');
INSERT INTO "django_migrations"
VALUES (25, 'sites', '0002_alter_domain_unique', '2024-03-04 17:06:15.386330');
INSERT INTO "django_migrations"
VALUES (26, 'socialaccount', '0001_initial', '2024-03-04 17:06:15.397618');
INSERT INTO "django_migrations"
VALUES (27, 'socialaccount', '0002_token_max_lengths', '2024-03-04 17:06:15.406532');
INSERT INTO "django_migrations"
VALUES (28, 'socialaccount', '0003_extra_data_default_dict', '2024-03-04 17:06:15.410561');
INSERT INTO "django_migrations"
VALUES (29, 'socialaccount', '0004_app_provider_id_settings', '2024-03-04 17:06:15.418334');
INSERT INTO "django_migrations"
VALUES (30, 'socialaccount', '0005_socialtoken_nullable_app', '2024-03-04 17:06:15.423733');
INSERT INTO "django_migrations"
VALUES (31, 'socialaccount', '0006_alter_socialaccount_extra_data', '2024-03-05 19:32:02.166715');
INSERT INTO "django_migrations"
VALUES (32, 'WEB', '0001_initial', '2024-03-06 12:45:07.784655');
INSERT INTO "django_migrations"
VALUES (33, 'WEB', '0002_profile', '2024-03-20 14:20:18.378383');
INSERT INTO "django_migrations"
VALUES (34, 'WEB', '0003_profile_level', '2024-03-20 14:20:18.383644');
INSERT INTO "django_migrations"
VALUES (35, 'WEB', '0004_rename_google_id_profile_profile_id', '2024-03-20 14:20:18.388003');
INSERT INTO "django_migrations"
VALUES (36, 'WEB', '0005_rename_profile_id_profile_google_id', '2024-03-20 14:20:18.392762');
INSERT INTO "django_migrations"
VALUES (37, 'WEB', '0006_alter_profile_google_id', '2024-03-20 14:20:18.397621');
INSERT INTO "django_migrations"
VALUES (38, 'WEB', '0007_video', '2024-03-20 14:20:18.398753');
INSERT INTO "django_migrations"
VALUES (39, 'form', '0001_initial', '2024-03-25 14:44:36.115671');
INSERT INTO "django_migrations"
VALUES (40, 'feedback', '0001_initial', '2024-03-25 15:26:01.162680');
INSERT INTO "django_migrations"
VALUES (41, 'Forum', '0001_initial', '2024-03-26 12:42:38.443161');
INSERT INTO "django_migrations"
VALUES (42, 'WEB', '0008_userprofile_events', '2024-03-29 11:28:19.404752');
INSERT INTO "django_migrations"
VALUES (43, 'WEB', '0009_personalcalendar', '2024-03-29 14:03:28.077960');
INSERT INTO "django_migrations"
VALUES (44, 'WEB', '0010_task', '2024-03-29 14:08:38.673736');
INSERT INTO "django_migrations"
VALUES (45, 'WEB', '0011_task_last_reset', '2024-03-29 14:14:57.205544');
INSERT INTO "django_migrations"
VALUES (46, 'WEB', '0012_task_time', '2024-03-29 14:26:57.124573');
INSERT INTO "django_migrations"
VALUES (47, 'WEB', '0013_remove_task_date_alter_task_time', '2024-03-29 14:29:26.070300');
INSERT INTO "django_migrations"
VALUES (48, 'WEB', '0014_remove_video_create_at_remove_video_file_and_more', '2024-03-30 15:28:02.275157');
INSERT INTO "django_migrations"
VALUES (49, 'WEB', '0015_video_image_alter_task_time', '2024-03-30 15:31:20.941608');
INSERT INTO "django_migrations"
VALUES (50, 'WEB', '0016_alter_task_time_alter_video_image', '2024-03-30 15:37:19.118755');
INSERT INTO "django_migrations"
VALUES (51, 'WEB', '0017_remove_video_image_video_image_url_alter_task_time', '2024-03-30 15:53:15.238237');
INSERT INTO "django_migrations"
VALUES (52, 'WEB', '0018_alter_task_time', '2024-03-31 18:40:51.875836');
INSERT INTO "django_migrations"
VALUES (53, 'WEB', '0019_alter_task_time', '2024-04-02 13:57:17.849247');
INSERT INTO "django_migrations"
VALUES (54, 'WEB', '0020_alter_task_time', '2024-04-02 13:57:17.857693');
INSERT INTO "django_migrations"
VALUES (55, 'WEB', '0021_alter_task_time', '2024-04-02 13:57:17.862996');
INSERT INTO "django_migrations"
VALUES (56, 'WEB', '0022_alter_task_time', '2024-04-02 13:57:17.868311');
INSERT INTO "django_migrations"
VALUES (57, 'WEB', '0023_alter_task_time', '2024-04-02 13:57:17.873608');
INSERT INTO "django_migrations"
VALUES (58, 'WEB', '0024_alter_task_time', '2024-04-02 13:57:17.879570');
INSERT INTO "django_migrations"
VALUES (59, 'WEB', '0025_alter_task_time', '2024-04-02 13:57:17.885602');
INSERT INTO "django_migrations"
VALUES (60, 'WEB', '0026_alter_task_time', '2024-04-02 13:57:17.890741');
INSERT INTO "django_migrations"
VALUES (61, 'WEB', '0027_alter_task_time', '2024-04-02 13:57:17.895865');
INSERT INTO "django_migrations"
VALUES (62, 'WEB', '0028_alter_task_time', '2024-04-02 13:57:17.901328');
INSERT INTO "django_migrations"
VALUES (63, 'WEB', '0029_alter_task_time', '2024-04-02 13:57:17.906441');
INSERT INTO "django_migrations"
VALUES (64, 'WEB', '0030_profile_profile_picture_alter_task_time', '2024-04-02 15:12:46.373681');
INSERT INTO "django_migrations"
VALUES (65, 'WEB', '0031_remove_profile_profile_picture_alter_task_time', '2024-04-02 15:14:28.611703');
INSERT INTO "django_migrations"
VALUES (66, 'Forum', '0002_post_parent_post', '2024-04-02 15:20:31.174086');
INSERT INTO "django_migrations"
VALUES (67, 'WEB', '0032_alter_task_time', '2024-04-02 15:20:31.180160');
INSERT INTO "django_migrations"
VALUES (68, 'Forum', '0003_remove_post_parent_post_response', '2024-04-02 15:40:13.458694');
INSERT INTO "django_migrations"
VALUES (69, 'WEB', '0033_alter_task_time', '2024-04-02 15:40:13.464416');
INSERT INTO "django_migrations"
VALUES (70, 'WEB', '0034_alter_task_time', '2024-04-02 15:57:00.549852');
INSERT INTO "django_migrations"
VALUES (71, 'WEB', '0035_taskcategory_alter_task_time_task_category_and_more', '2024-04-02 16:03:21.915327');
CREATE TABLE "django_session"
(
    "session_key"  varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text        NOT NULL,
    "expire_date"  datetime    NOT NULL
);
INSERT INTO "django_session"
VALUES ('lxch012bi990ogbmud1pa9n3g2zcey1d',
        '.eJxVjr1uwzAMhN-Fc-BGgn7gbCmQIe3QsUNRGBRN1EJcybVkIECQdy8deGg38u67I2_Q4VKHbik8d7GHAyjY_dUC0oXTauA4rnKDRHlJtXkwm12ao2ycaiSsMafnLfWvasAySI91ygfNXnMw7J1pW89aGQyOes0iWm_0fo8tuRCUsmhZCFK9qGiskdKSKeK4PdKVipXh8HGDxNcqF54EmeZMXIpsY_6KaQ1RngQDGR8_TTjj9wrAfQen9x-6Hl_bcz2_nV4mB5_3X3cRXTQ:1rhQqn:EZHYuTrH6TSWW-PLlGTKiplvQwjaW7Ke_ESpEQyerjo',
        '2024-03-19 09:12:41.022456');
INSERT INTO "django_session"
VALUES ('qrznbzlkxz56m3r64zg4b4pgbdasadkz',
        '.eJxVjksOgzAMRO-SdYXs_MOuvUjk_AQqClIJq6p3L6As2uXM2G_mzTztbfL7ll9-TmxknN1-vUDxmesZ0LKc9kAxrnttw3XT4224HyrXNkdq81of_esPNdE2HRwpiwAglMJobQRIF0iVlKNAm3MiCIpbEGC1LeiQBy6CUgUDJJuiO_f1CRe7l-bkqbERDTgtpRR6QIMW8PMFd_xJmw:1rhUcG:47lthHjTc3DWNnxNfA_cq815-0t4s6TutG2f8as59Ro',
        '2024-03-19 13:13:56.172840');
INSERT INTO "django_session"
VALUES ('eebse72qakukkakmsvxk8jwsclvxbnzs',
        '.eJxlUMluhDAM_RefEXIWsnBrf6OqIhPCEJWSCsJcRvPvEygX2pv1Nj_7AeR92ubsaMtjmHP0lGOa3XfIY-pXaD8e8DtDC2vykabTARVQhpZptJpzZUStrLLaVvCzpHvsw1Ict5RuUyjSLe4BjEmGpjEKjbQcBcdGMXh-VnDsd9saFncoBVywjvxXmHeCpmmH67NFfWhOeq3fLle8n65L1EjrWHKkl6U6H0yHnlmte9FYUqj4EBrDtfBeI5IgGVDrDnlHWDQDUw23lrzaz___utC7P08pKVw-X0rXcwo:1rhoyJ:AWwVRXfxRnUtYnLcaFd8-YrghlJ_VJBtybL7VyZkoKs',
        '2024-03-20 10:58:03.700951');
INSERT INTO "django_session"
VALUES ('tciui0gxzsvwhb8p1ceaouo3m1pkn3gm',
        '.eJxlUEtuhDAMvYvXCDn_hF17jaqKTAhDVEoqCLMZzd0HKBvanfV-fvYDKIS8TsXTWoY4lRSopDz571iG3C3QfDzgd4YGlhwSjacDKqACDTPoDLdc85pJIYSr4GfO99TFeXPccr6NcZOuaQ9gTDK0ymq00nEUHJVm8Pys4Njv1yXO_lAKuGAtha847QSN4w7XZ4v60Jz0Ur9drng_XZeogZZhy5FBbtV5b1sMzBnTCeVIo-Z9VJYbEYJBJEEyojEt8pZw0_RMK-4cBb2f__91sfN_n6K00PL5AqN6cy0:1rhqQI:msvfh4w5Ej8nWJhxAhr6GH6Q8xHU1YZkLr1u-hOPI8I',
        '2024-03-20 12:31:02.157922');
INSERT INTO "django_session"
VALUES ('vk5zvxlhb8ezxvx9d6hcobwy7tcdxbqe',
        '.eJxlUMluhDAM_RefEXIWsnBrf6OqIhPCEJWSCsJcRvPvEygX2pv1Nj_7AeR92ubsaMtjmHP0lGOa3XfIY-pXaD8e8DtDC2vykabTARVQhpZptJpbrbHmSmshK_hZ0j32YSmOW0q3KRTpFvcAxiRD0xiFRlqOgmOjGDw_Kzj2u20NizuUAi5YR_4rzDtB07TD9dmiPjQnvdZvlyveT9claqR1LDnSy1KdD6ZDz0r9XjSWFCo-hMZwLbzXiCRIBtS6Q94RFs3AVMOtJa_28_-_LvTu71MMMsOeL6_3czg:1rhqoc:JbFa8djatef2y3fG9pHZB03Fg6sj7WXFPYdPebSJNO8',
        '2024-03-20 12:56:10.281876');
INSERT INTO "django_session"
VALUES ('f0hmidajym1ept1zco309ux3eg4t44yk',
        '.eJxVjMEOwiAQRP-FsyFAV6De9EeaZXcNxIYmQk_Gf7c1Pehx3sy8l5pw7XlamzynwuqirDr9soT0kLoXOM871ki0rLXr7-aom75uSWovhL0s9Xa8_lQZW948bvRigcB74GDBBGBxQ0zk2RkGhDSkwUQrZuTojDhijGfLSCaG8R7U-wOcpDvb:1ritAo:fkpAuXMpTIx1z22v9A5bKzIeEziJ44jVU9UBIG8fyuc',
        '2024-03-23 09:39:22.978438');
INSERT INTO "django_session"
VALUES ('daxv5vtwdfne3odcqys86fgwyr9hz1xg',
        '.eJxlUMtuhDAQ-5c5I5TJO3trf6Oq0DAJCyolFYReVvvvBcqF9jby2JbtBxBzXqfS0Fr6NJWBqQx5aj5T6XNc4Pb2gN8bbrBkHmg8FVABFbihQxTSCpS1MlpgkBV8zfl7iGneJPec72PauOuwOyB6YVxw3iolFW58bRGe7xUcAZp1SXNzMDVcsJb4I037g8Zxh-szRn1wzvdSv1xqvJ6qi1VPS7_5CLaeGIPFjoUygqSW3HZadUlq73WrZZAOpYsuUDQtek6d40BoYutN2Pv_3y7F5u8qFgW65w8RwHPS:1rnI1k:c2bXBlAZkcMOTqerxp6sv2DkTgHMNHlGlNab3BVWTcc',
        '2024-04-04 13:00:12.362121');
INSERT INTO "django_session"
VALUES ('fj3zhcyer5uv6kn550gxjelqjzxu2046',
        '.eJxVjMEOwiAQRP-FsyFAV6De9EeaZXcNxIYmQk_Gf7c1Pehx3sy8l5pw7XlamzynwuqirDr9soT0kLoXOM871ki0rLXr7-aom75uSWovhL0s9Xa8_lQZW948bvRigcB74GDBBGBxQ0zk2RkGhDSkwUQrZuTojDhijGfLSCaG8R7U-wOcpDvb:1rpoc9:iy5Ds7eq1DRmsi_nASRLVf5daUfeeTg3A0jTg6ZXLKI',
        '2024-04-11 12:12:13.168747');
INSERT INTO "django_session"
VALUES ('5o7cwrvfxgh03au1bjonc57u4szzuqgd',
        '.eJxVjMEOwiAQRP-FsyFAV6De9EeaZXcNxIYmQk_Gf7c1Pehx3sy8l5pw7XlamzynwuqirDr9soT0kLoXOM871ki0rLXr7-aom75uSWovhL0s9Xa8_lQZW948bvRigcB74GDBBGBxQ0zk2RkGhDSkwUQrZuTojDhijGfLSCaG8R7U-wOcpDvb:1rrgW9:u4sZDWcAvXHHMC-SvR1sRR85duoOUbSwYWCdQY6gLU0',
        '2024-04-16 15:57:45.704318');
CREATE TABLE "django_site"
(
    "id"     integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name"   varchar(50)  NOT NULL,
    "domain" varchar(100) NOT NULL UNIQUE
);
INSERT INTO "django_site"
VALUES (1, 'calm-connections.azurewebsites.net', 'calm-connections.azurewebsites.net');
INSERT INTO "django_site"
VALUES (2, 'localhost', 'http://127.0.0.1:8000/');
CREATE TABLE "feedback_feedback"
(
    "id"            integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "customer_name" varchar(120) NOT NULL,
    "email"         varchar(254) NOT NULL,
    "details"       text         NOT NULL,
    "happy"         bool         NOT NULL,
    "date"          date         NOT NULL,
    "product_id"    bigint       NOT NULL REFERENCES "feedback_product" ("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "feedback_feedback"
VALUES (1, 'Dmytro', 'exe24876@gmail.com', 'No good', 0, '2024-03-25', 1);
INSERT INTO "feedback_feedback"
VALUES (2, 'Dmytro', 'exe24876@gmail.com', 'gyrfhwndjdcswru35rfsnfsq', 1, '2024-03-26', 1);
INSERT INTO "feedback_feedback"
VALUES (3, 'Dmytro', 'exe24876@gmail.com', 'Bad', 0, '2024-03-27', 1);
CREATE TABLE "feedback_product"
(
    "id"   integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(120) NOT NULL
);
INSERT INTO "feedback_product"
VALUES (1, 'Customization');
CREATE TABLE "form_feedback"
(
    "id"            integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "customer_name" varchar(120) NOT NULL,
    "email"         varchar(254) NOT NULL,
    "details"       text         NOT NULL,
    "happy"         bool         NOT NULL,
    "date"          date         NOT NULL,
    "product_id"    bigint       NOT NULL REFERENCES "form_product" ("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "form_feedback"
VALUES (1, 'Dmytro', 'exe24876@gmail.com', 'Very good', 1, '2024-03-25', 3);
CREATE TABLE "form_product"
(
    "id"   integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(120) NOT NULL
);
INSERT INTO "form_product"
VALUES (1, 'Authorization');
INSERT INTO "form_product"
VALUES (2, 'Customization');
INSERT INTO "form_product"
VALUES (3, 'Guided Meditation');
CREATE TABLE "socialaccount_socialaccount"
(
    "id"          integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "provider"    varchar(200) NOT NULL,
    "uid"         varchar(191) NOT NULL,
    "last_login"  datetime     NOT NULL,
    "date_joined" datetime     NOT NULL,
    "user_id"     integer      NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "extra_data"  text         NOT NULL CHECK ((JSON_VALID("extra_data") OR "extra_data" IS NULL))
);
INSERT INTO "socialaccount_socialaccount"
VALUES (3, 'google', '118057978633231401461', '2024-03-27 17:49:21.892616', '2024-03-20 14:31:53.424177', 4,
        '{"iss": "https://accounts.google.com", "azp": "172466701375-qqt3sji1pgnfk55clalbdjevlft7tset.apps.googleusercontent.com", "aud": "172466701375-qqt3sji1pgnfk55clalbdjevlft7tset.apps.googleusercontent.com", "sub": "118057978633231401461", "email": "dima.bilik2005@gmail.com", "email_verified": true, "at_hash": "bT5KOot1BXKPL2ifmpCgbw", "name": "DIma Bilik", "picture": "https://lh3.googleusercontent.com/a/ACg8ocIHRyhOVuNb5Opa2E5nSyaR_uxoUZF1xD5vH8wJgnSI=s96-c", "given_name": "DIma", "family_name": "Bilik", "iat": 1711561761, "exp": 1711565361}');
INSERT INTO "socialaccount_socialaccount"
VALUES (4, 'google', '107885591332829168028', '2024-04-02 13:57:50.955161', '2024-04-02 13:57:50.955198', 5,
        '{"iss": "https://accounts.google.com", "azp": "172466701375-qqt3sji1pgnfk55clalbdjevlft7tset.apps.googleusercontent.com", "aud": "172466701375-qqt3sji1pgnfk55clalbdjevlft7tset.apps.googleusercontent.com", "sub": "107885591332829168028", "email": "exe24876@gmail.com", "email_verified": true, "at_hash": "qVXNhVZlCWb8X0RIhAODqA", "name": "Dmytro", "picture": "https://lh3.googleusercontent.com/a/ACg8ocKoXHpOBbw4jT68IMzdlblnE7ZvLW788jLJhUOEfurl=s96-c", "given_name": "Dmytro", "iat": 1712066270, "exp": 1712069870}');
CREATE TABLE "socialaccount_socialapp"
(
    "id"          integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "provider"    varchar(30)  NOT NULL,
    "name"        varchar(40)  NOT NULL,
    "client_id"   varchar(191) NOT NULL,
    "secret"      varchar(191) NOT NULL,
    "key"         varchar(191) NOT NULL,
    "provider_id" varchar(200) NOT NULL,
    "settings"    text         NOT NULL CHECK ((JSON_VALID("settings") OR "settings" IS NULL))
);
INSERT INTO "socialaccount_socialapp"
VALUES (1, 'google', 'Google Authorization', '172466701375-qqt3sji1pgnfk55clalbdjevlft7tset.apps.googleusercontent.com',
        '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', '', '', '{}');
CREATE TABLE "socialaccount_socialapp_sites"
(
    "id"           integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "socialapp_id" integer NOT NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED,
    "site_id"      integer NOT NULL REFERENCES "django_site" ("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "socialaccount_socialapp_sites"
VALUES (1, 1, 1);
INSERT INTO "socialaccount_socialapp_sites"
VALUES (2, 1, 2);
CREATE TABLE "socialaccount_socialtoken"
(
    "id"           integer  NOT NULL PRIMARY KEY AUTOINCREMENT,
    "token"        text     NOT NULL,
    "token_secret" text     NOT NULL,
    "expires_at"   datetime NULL,
    "account_id"   integer  NOT NULL REFERENCES "socialaccount_socialaccount" ("id") DEFERRABLE INITIALLY DEFERRED,
    "app_id"       integer  NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "account_emailconfirmation_email_address_id_5b7f8c58" ON "account_emailconfirmation" ("email_address_id");
CREATE UNIQUE INDEX "account_emailaddress_user_id_email_987c8728_uniq" ON "account_emailaddress" ("user_id", "email");
CREATE UNIQUE INDEX "unique_verified_email" ON "account_emailaddress" ("email") WHERE "verified";
CREATE INDEX "account_emailaddress_user_id_2c513194" ON "account_emailaddress" ("user_id");
CREATE INDEX "account_emailaddress_upper" ON "account_emailaddress" ((UPPER("email")));
CREATE UNIQUE INDEX "socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq" ON "socialaccount_socialapp_sites" ("socialapp_id", "site_id");
CREATE INDEX "socialaccount_socialapp_sites_socialapp_id_97fb6e7d" ON "socialaccount_socialapp_sites" ("socialapp_id");
CREATE INDEX "socialaccount_socialapp_sites_site_id_2579dee5" ON "socialaccount_socialapp_sites" ("site_id");
CREATE UNIQUE INDEX "socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq" ON "socialaccount_socialtoken" ("app_id", "account_id");
CREATE INDEX "socialaccount_socialtoken_account_id_951f210e" ON "socialaccount_socialtoken" ("account_id");
CREATE INDEX "socialaccount_socialtoken_app_id_636a42d7" ON "socialaccount_socialtoken" ("app_id");
CREATE UNIQUE INDEX "socialaccount_socialaccount_provider_uid_fc810c6e_uniq" ON "socialaccount_socialaccount" ("provider", "uid");
CREATE INDEX "socialaccount_socialaccount_user_id_8146e70c" ON "socialaccount_socialaccount" ("user_id");
CREATE INDEX "form_feedback_product_id_00de3cd6" ON "form_feedback" ("product_id");
CREATE INDEX "feedback_feedback_product_id_a2a8cf45" ON "feedback_feedback" ("product_id");
CREATE INDEX "Forum_post_user_id_9c46af4a" ON "Forum_post" ("user_id");
CREATE INDEX "Forum_response_parent_post_id_ba0d6e96" ON "Forum_response" ("parent_post_id");
CREATE INDEX "WEB_task_user_id_f6a269dc" ON "WEB_task" ("user_id");
CREATE INDEX "WEB_task_category_id_c7333942" ON "WEB_task" ("category_id");
DELETE
FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence"
VALUES ('django_migrations', 71);
INSERT INTO "sqlite_sequence"
VALUES ('django_admin_log', 39);
INSERT INTO "sqlite_sequence"
VALUES ('django_content_type', 24);
INSERT INTO "sqlite_sequence"
VALUES ('auth_permission', 96);
INSERT INTO "sqlite_sequence"
VALUES ('auth_group', 0);
INSERT INTO "sqlite_sequence"
VALUES ('auth_user', 5);
INSERT INTO "sqlite_sequence"
VALUES ('account_emailaddress', 4);
INSERT INTO "sqlite_sequence"
VALUES ('django_site', 2);
INSERT INTO "sqlite_sequence"
VALUES ('socialaccount_socialapp', 1);
INSERT INTO "sqlite_sequence"
VALUES ('socialaccount_socialtoken', 0);
INSERT INTO "sqlite_sequence"
VALUES ('socialaccount_socialapp_sites', 2);
INSERT INTO "sqlite_sequence"
VALUES ('socialaccount_socialaccount', 4);
INSERT INTO "sqlite_sequence"
VALUES ('WEB_profile', 3);
INSERT INTO "sqlite_sequence"
VALUES ('form_product', 3);
INSERT INTO "sqlite_sequence"
VALUES ('form_feedback', 1);
INSERT INTO "sqlite_sequence"
VALUES ('feedback_product', 1);
INSERT INTO "sqlite_sequence"
VALUES ('feedback_feedback', 3);
INSERT INTO "sqlite_sequence"
VALUES ('WEB_userprofile', 5);
INSERT INTO "sqlite_sequence"
VALUES ('WEB_video', 3);
INSERT INTO "sqlite_sequence"
VALUES ('Forum_post', 24);
INSERT INTO "sqlite_sequence"
VALUES ('WEB_task', 2);
INSERT INTO "sqlite_sequence"
VALUES ('WEB_taskcategory', 1);
COMMIT;
